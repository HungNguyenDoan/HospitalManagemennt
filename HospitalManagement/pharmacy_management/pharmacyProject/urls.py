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
    path('api/pharmacy/create/', MedicalSupplyCreateAPIView.as_view(), name='pharmacy_create'),
    path('api/pharmacy/<int:id>/', MedicalSupplyDetailAPIView.as_view(), name='pharmacy_detail'),
    path('api/pharmacy/update/<int:id>/', MedicalSupplyUpdateAPIView.as_view(), name='pharmacy_update'),
    path('api/pharmacy/delete/<int:id>/', MedicalSupplyDeleteAPIView.as_view(), name='pharmacy_delete'),
    path('api/pharmacy/type/all/', MedicalSupplyListByTypeAPIView.as_view(), name='pharmacy_list_by_type'),
    path('api/pharmacy/search/', MedicalSupplySearchAPIView.as_view(), name='pharmacy_search'),
]
