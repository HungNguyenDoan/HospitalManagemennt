from django.urls import path
from .views import *
urlpatterns = [
    path('patients/register', RegisterView.as_view(), name='register'),
    path('patients/login', LoginView.as_view(), name='login'),
    path('patients', GetAllPatient.as_view(), name='get-all'),
    path('patients/<int:id>', GetPatientDetail.as_view(), name='patient-update'),
    path('patients/update/<int:id>', UpdateInfoPatient.as_view(), name='patient-update'),
    path('patients/delete/<int:id>', DeletePatient.as_view(), name='patient-update'),
    path('patients/doctors/<int:doctor_id>',GetPatientByDoctor.as_view(), name='patient-doctor'),
    path('patients/search',SearchPatient.as_view(), name='search'),
    path('health_records/create',CreateHealthRecord.as_view(), name='create-health-record'),
    path('health_records',GetAllHealthRecord.as_view(), name='get-all-health'),
    path('health_records/<int:patient_id>',GetHealthRecordPatient.as_view(), name='get-patient-health'),
    path('health_records/update/<int:health_record_id>',UpdateHealthRecord.as_view(), name='update-patient-health'),
    path('health_records/delete/<int:health_record_id>',DeleteHealthRecord.as_view(), name='delete-patient-health'),

]