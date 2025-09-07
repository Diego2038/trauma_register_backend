from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework import status
from unittest.mock import patch, MagicMock
from custom_user.views import (
    UserViewset,
    VerifyTokenView,
    login
)
from custom_user.serializers import UserSerializer
from custom_user.models import CustomUser

User = get_user_model()

class UserViewsetTest(TestCase):
  def setUp(self):
    self.factory = APIRequestFactory()
    self.user = User.objects.create_user(
      username="testuser",
      password="oldpassword",
      email="test@example.com",
    )
    self.another_user = User.objects.create_user(
      username="anotheruser",
      password="12345",
      email="another@example.com",
    )
    self.viewset = UserViewset.as_view({
      'get': 'retrieve',
      'put': 'update',
      'patch': 'partial_update',
      'post': 'create',
      'delete': 'destroy',
    })

  def test_retrieve_user(self):
    """Verifica que se puede obtener un usuario por su username."""
    request = self.factory.get(f'/users/{self.user.username}/')
    force_authenticate(request, user=self.user)
    response = self.viewset(request, username=self.user.username)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data['username'], self.user.username)

  @patch.object(UserViewset, 'get_serializer')
  def test_update_user_successful(self, mock_get_serializer):
    """Verifica que se puede actualizar un usuario sin la contraseña."""
    mock_serializer = MagicMock(spec=UserSerializer)
    mock_serializer.is_valid.return_value = True
    mock_serializer.data = {'username': 'NewName'}
    mock_get_serializer.return_value = mock_serializer

    request = self.factory.put(f'/users/{self.user.username}/', {'username': 'NewName'})
    force_authenticate(request, user=self.user)
    response = self.viewset(request, username=self.user.username)

    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data['username'], 'NewName')
    mock_serializer.is_valid.assert_called_once_with(raise_exception=True)
    self.assertTrue(mock_serializer.save.called)

  @patch('custom_user.views.UserSerializer')
  def test_update_with_password_raises_error(self, MockUserSerializer):
    """Verifica que se prohíba la actualización de la contraseña."""
    request = self.factory.put(f'/users/{self.user.username}/', {'password': 'newpassword'})
    force_authenticate(request, user=self.user)
    response = self.viewset(request, username=self.user.username)
    self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    self.assertEqual(response.data['error'], "It's forbidden update the password, contact the admin please")

  def test_create_forbidden(self):
    """Verifica que la creación de usuarios esté prohibida."""
    request = self.factory.post('/users/', {'username': 'newuser'})
    force_authenticate(request, user=self.user)
    response = self.viewset(request)
    self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    self.assertEqual(response.data['error'], "It's forbidden to do this action")

  def test_destroy_forbidden(self):
    """Verifica que la eliminación de usuarios esté prohibida."""
    request = self.factory.delete(f'/users/{self.user.username}/')
    force_authenticate(request, user=self.user)
    response = self.viewset(request, username=self.user.username)
    self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    self.assertEqual(response.data['error'], "It's forbidden to do this action")

class VerifyTokenViewTest(TestCase):
    def setUp(self):
      self.factory = APIRequestFactory()
      self.user = User.objects.create_user(
        username="testuser",
        password="12345",
        email="test@example.com",
      )
      self.view = VerifyTokenView.as_view({'get': 'list'})

    def test_token_is_valid(self):
      """Verifica que la vista retorna un 200 OK cuando el token es válido."""
      request = self.factory.get('/verify-token/')
      force_authenticate(request, user=self.user)
      response = self.view(request)
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertEqual(response.data['response'], "Token válido")

class LoginViewTest(TestCase):
  def setUp(self):
    self.factory = APIRequestFactory()
    self.user = User.objects.create_user(
      username="testuser",
      password="correct_password",
      email="test@example.com",
    )
    self.request_data_ok = {'username': 'testuser', 'password': 'correct_password'}
    self.request_data_wrong_pass = {'username': 'testuser', 'password': 'wrong_password'}
    self.request_data_invalid_user = {'username': 'nonexistent_user', 'password': 'any_password'}

  @patch('custom_user.views.UserSerializer')
  @patch('custom_user.views.RefreshToken')
  @patch('custom_user.views.get_object_or_404')
  def test_login_successful(self, mock_get_object_or_404, MockRefreshToken, MockUserSerializer):
    """Verifica que el login sea exitoso con credenciales correctas."""
    # Configurar mocks
    mock_get_object_or_404.return_value = self.user
    self.user.check_password = MagicMock(return_value=True)

    mock_refresh_token = MagicMock()
    mock_refresh_token.access_token = 'mock_access_token'
    mock_refresh_token.return_value = 'mock_refresh_token'
    MockRefreshToken.for_user.return_value = mock_refresh_token

    mock_user_serializer = MagicMock(spec=UserSerializer)
    mock_user_serializer.data = {'username': 'testuser', 'email': 'test@example.com'}
    MockUserSerializer.return_value = mock_user_serializer
    
    # Simular la solicitud
    request = self.factory.post('/login/', data=self.request_data_ok, format='json')
    response = login(request)

    # Aserciones
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertIn('token', response.data)
    self.assertIn('token_refresh', response.data)
    self.assertIn('user', response.data)
    self.user.check_password.assert_called_once_with('correct_password')

  @patch('custom_user.views.get_object_or_404')
  def test_login_with_wrong_password(self, mock_get_object_or_404):
    """Verifica que el login falle con una contraseña incorrecta."""
    # Configurar mock del usuario
    mock_get_object_or_404.return_value = self.user
    self.user.check_password = MagicMock(return_value=False)

    # Simular la solicitud
    request = self.factory.post('/login/', data=self.request_data_wrong_pass, format='json')
    response = login(request)

    # Aserciones
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    self.assertEqual(response.data['error'], "Invalid password")

  def test_login_with_nonexistent_user(self):
    """Verifica que el login falle para un usuario que no existe."""
    request = self.factory.post('/login/', data=self.request_data_invalid_user, format='json')
    response = login(request)

    # Aserciones
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class LoginViewTest(TestCase):
  def setUp(self):
    self.factory = APIRequestFactory()

  @patch('custom_user.views.get_object_or_404')
  def test_login_invalid_password(self, mock_get_object):
    # Mock del usuario
    mock_user = MagicMock()
    mock_user.check_password.return_value = False
    mock_get_object.return_value = mock_user

    # Request real de DRF
    request = self.factory.post("/", {"username": "testuser", "password": "wrong"}, format="json")
    response = login(request)

    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    self.assertEqual(response.data, {"error": "Invalid password"})

  @patch('custom_user.views.UserSerializer')
  @patch('custom_user.views.RefreshToken.for_user')
  @patch('custom_user.views.get_object_or_404')
  def test_login_successful(self, mock_get_object, mock_for_user, mock_serializer):
    # Mock del usuario
    mock_user = MagicMock()
    mock_user.check_password.return_value = True
    mock_get_object.return_value = mock_user

    # Mock del token
    mock_token = MagicMock()
    mock_token.__str__ = lambda s: "refresh_token"
    mock_token.access_token = "access_token"
    mock_for_user.return_value = mock_token

    # Mock del serializer
    mock_serializer_instance = MagicMock()
    mock_serializer_instance.data = {"username": "testuser"}
    mock_serializer.return_value = mock_serializer_instance

    # Request real de DRF
    request = self.factory.post("/", {"username": "testuser", "password": "12345"}, format="json")
    response = login(request)

    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data, {
      "token": "access_token",
      "token_refresh": "refresh_token",
      "user": {"username": "testuser"}
    })
    mock_get_object.assert_called_once_with(CustomUser, username="testuser")
    mock_for_user.assert_called_once_with(mock_user)
    mock_serializer.assert_called_once_with(instance=mock_user)