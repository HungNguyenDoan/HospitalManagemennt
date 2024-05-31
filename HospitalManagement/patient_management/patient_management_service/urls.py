from django.urls import path
from .views import *
urlpatterns = [
    path('patients/create', PatientCreateAPIView.as_view(), name='register'),
    path('patients/login', PatientLoginAPIView.as_view(), name='login'),
    path('patients', GetAllPatientAPIView.as_view(), name='get-all'),
    path('patients/<int:id>', GetPatientDetailAPIView.as_view(), name='patient-update'),
    path('patients/update/<int:id>', UpdatePatientAPIView.as_view(), name='patient-update'),
    path('patients/delete/<int:id>', DeletePatientAPIView.as_view(), name='patient-update'),
    path('patients/doctors/<int:doctor_id>',PatientListByDoctorAPIView.as_view(), name='patient-doctor'),
    path('patients/search',PatientSearchAPIView.as_view(), name='search'),
]