from django.urls import path
from .views import (
    DoctorCreateView, DoctorDetailView, DoctorUpdateView,
    DoctorDeleteView, SearchDoctorsView, LoginView, LogoutView, UserRegistrationView
)

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', DoctorCreateView.as_view(), name='doctor-create'),
    path('<int:id>/', DoctorDetailView.as_view(), name='doctor-detail'),
    path('update/<int:id>/', DoctorUpdateView.as_view(), name='doctor-update'),
    path('delete/<int:id>/', DoctorDeleteView.as_view(), name='doctor-delete'),
    path('search/', SearchDoctorsView.as_view(), name='doctor-search'),
    path('user/register/', UserRegistrationView.as_view(), name='user-register'),
]