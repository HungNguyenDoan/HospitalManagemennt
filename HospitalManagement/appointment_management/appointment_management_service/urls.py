from django.contrib import admin
from django.urls import path
from appointment_management_service.views import (
    AppointmentCreateAPIView,
    AppointmentDetailAPIView,
    AppointmentUpdateAPIView,
    AppointmentDeleteAPIView,
    AppointmentListByDoctorOrPatientAPIView,
    AppointmentListByDoctorOrPatientAndDateAPIView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schedules/patients/create', AppointmentCreateAPIView.as_view(), name='appointment-create'),
    path('api/schedules/<int:id>', AppointmentDetailAPIView.as_view(), name='appointment-detail'),
    path('api/schedules/update/<int:id>', AppointmentUpdateAPIView.as_view(), name='appointment-update'),
    path('api/schedules/delete/<int:id>', AppointmentDeleteAPIView.as_view(), name='appointment-delete'),
    path('api/schedules', AppointmentListByDoctorOrPatientAndDateAPIView.as_view(), name='appointment-list-by-date'),
    path('api/schedules', AppointmentListByDoctorOrPatientAPIView.as_view(), name='appointment-list'),
]
