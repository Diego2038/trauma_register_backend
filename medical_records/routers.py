from rest_framework.routers import DefaultRouter
from .views import PatientDataViewsets

router = DefaultRouter()

router.register(r'patient-data', PatientDataViewsets, basename='patient-data')

urlpatterns = router.urls