from django.urls import path
from .views import (
    MedicalSupplyCreateAPIView,
    MedicalSupplyDetailAPIView,
    MedicalSupplyUpdateAPIView,
    MedicalSupplyDeleteAPIView,
    MedicalSupplyListByTypeAPIView,
    MedicalSupplySearchAPIView
)

urlpatterns = [
    path('pharmacy/create', MedicalSupplyCreateAPIView.as_view(), name='pharmacy_create'),
    path('pharmacy/<int:id>', MedicalSupplyDetailAPIView.as_view(), name='pharmacy_detail'),
    path('pharmacy/update/<int:id>', MedicalSupplyUpdateAPIView.as_view(), name='pharmacy_update'),
    path('pharmacy/delete/<int:id>', MedicalSupplyDeleteAPIView.as_view(), name='pharmacy_delete'),
    path('pharmacy/type/all', MedicalSupplyListByTypeAPIView.as_view(), name='pharmacy_list_by_type'),
    path('pharmacy/search', MedicalSupplySearchAPIView.as_view(), name='pharmacy_search'),
]
