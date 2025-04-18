from rest_framework.routers import DefaultRouter
from .views import UserViewset, login, VerifyTokenView
from django.urls import path

router = DefaultRouter()

router.register(r'user', UserViewset, basename='user')
router.register(r'verify-token', VerifyTokenView, basename='verify-token')

urlpatterns = router.urls + [
  path('login/', login, name='login'),
]