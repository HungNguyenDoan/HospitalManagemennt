from django.urls import path
from medical_record.views import MedicalRecordAPIView

urlpatterns = [
    path('api/medical-records/', MedicalRecordAPIView.as_view(), name='medical-record-list'),
    path('api/medical-records/<int:pk>/', MedicalRecordAPIView.as_view(), name='medical-record-detail'),
]