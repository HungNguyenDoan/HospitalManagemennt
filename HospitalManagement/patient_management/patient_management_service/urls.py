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
]