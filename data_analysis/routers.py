from rest_framework.routers import DefaultRouter
from .views import AmountOfPatientDataStatsViewSet, PatientGenderStatsViewSet, PatientAgeStatsViewSet, PatientDataWithRelationsStatsViewSet, ObtainInsuredPatientsStatsViewSet, TypeOfPatientAdmissionStatsViewSet

router = DefaultRouter()

router.register('amount-of-patient-data-stats', AmountOfPatientDataStatsViewSet, basename='amount-of-patient-data-stats')
router.register('gender-stats', PatientGenderStatsViewSet, basename='gender-stats')
router.register('patient-age-stats', PatientAgeStatsViewSet, basename='patient-age-stats')
router.register('patient-with-relations-stats', PatientDataWithRelationsStatsViewSet, basename='patient-with-relations-stats')
urlpatterns = router.urls
router.register('obtain-insured-patients-stats', ObtainInsuredPatientsStatsViewSet, basename='obtain-insured-patients-stats')
urlpatterns = router.urls
router.register('type-of-patient-admission-stats', TypeOfPatientAdmissionStatsViewSet, basename='type-of-patient-admission-stats')
urlpatterns = router.urls