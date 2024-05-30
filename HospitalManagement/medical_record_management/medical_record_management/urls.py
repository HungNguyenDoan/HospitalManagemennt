from django.urls import path
from medical_record.views import MedicalRecordAPIView

urlpatterns = [
    # Other URL patterns...
    path('api/medical-records/', MedicalRecordAPIView.as_view(), name='medical-record-api'),
]
