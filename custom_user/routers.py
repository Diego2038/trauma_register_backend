from rest_framework.routers import DefaultRouter
from .views import UserViewset, login
from django.urls import path

router = DefaultRouter()

router.register(r'user', UserViewset, basename='user')

urlpatterns = router.urls + [
  path('login/', login, name='login'),
]