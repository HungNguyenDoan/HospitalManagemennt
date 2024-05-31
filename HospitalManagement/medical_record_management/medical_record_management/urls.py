from django.urls import path
from medical_record.views import (
    RecordCreateAPIView,
    RecordDetailAPIView,
    RecordUpdateAPIView,
    RecordListByPatientOrDoctorAPIView,
    RecordSearchAPIView,
)

urlpatterns = [
    path('api/records/create', RecordCreateAPIView.as_view(), name='record-create'),
    path('api/records/<int:id>', RecordDetailAPIView.as_view(), name='record-detail'),
    path('api/records/update/<int:id>', RecordUpdateAPIView.as_view(), name='record-update'),
    path('api/records', RecordListByPatientOrDoctorAPIView.as_view(), name='record-list-by-role'),
    path('api/records/patients/<int:patient_id>/search', RecordSearchAPIView.as_view(), name='record-search'),
]