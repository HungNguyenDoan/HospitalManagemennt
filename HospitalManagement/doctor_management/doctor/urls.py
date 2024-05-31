from django.urls import path
from .views import (
    DoctorCreateAPIView, DoctorDetailAPIView, DoctorUpdateAPIView,
    DoctorDeleteAPIView, DoctorSearchAPIView, DoctorLoginAPIView, DoctorLogoutAPIView
)

urlpatterns = [
    path('create/', DoctorCreateAPIView.as_view(), name='doctor-create'),
    path('<int:id>/', DoctorDetailAPIView.as_view(), name='doctor-detail'),
    path('update/<int:id>/', DoctorUpdateAPIView.as_view(), name='doctor-update'),
    path('delete/<int:id>/', DoctorDeleteAPIView.as_view(), name='doctor-delete'),
    path('search/', DoctorSearchAPIView.as_view(), name='doctor-search'),
]