from rest_framework.routers import DefaultRouter
from .views import PatientGenderStatsViewSet, PatientAgeStatsViewSet, PatientDataWithRelationsStatsViewSet

router = DefaultRouter()

router.register('gender-stats', PatientGenderStatsViewSet, basename='gender-stats')
router.register('patient-age-stats', PatientAgeStatsViewSet, basename='patient-age-stats')
router.register('patient-with-relations-stats', PatientDataWithRelationsStatsViewSet, basename='patient-with-relations-stats')
urlpatterns = router.urls