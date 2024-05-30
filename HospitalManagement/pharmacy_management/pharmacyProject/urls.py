from . import views
from django.urls import path, include

urlpatterns = [
    path('pharmacy', views.PharmacyGetAllAPIView.as_view(), name='pharmacy_list'),
    path('pharmacy/create', views.PharmacyCreateAPIView.as_view(), name='pharmacy_create'),
    path('pharmacy/<int:pk>/update', views.PharmacyUpdateAPIView.as_view(), name='pharmacy_update'),
    path('pharmacy/<int:pk>/delete', views.PharmacyDeleteAPIView.as_view(), name='pharmacy_delete'),
]
