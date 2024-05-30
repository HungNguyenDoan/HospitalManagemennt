from django.contrib import admin
from django.urls import path, include
from appointment_management_service.views import AppointmentList, AppointmentDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('schedules/patients/create', AppointmentList.as_view(), name='appointment-create'),
    path('schedules/<int:id>', AppointmentDetail.as_view(), name='appointment-detail'),
    path('schedules/update/<int:id>', AppointmentDetail.as_view(), name='appointment-update'),
    path('schedules/delete/<int:id>', AppointmentDetail.as_view(), name='appointment-delete'),
    path('schedules', AppointmentList.as_view(), name='appointment-list'),
]
