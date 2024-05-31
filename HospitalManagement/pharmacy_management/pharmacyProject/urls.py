from django.urls import path
from . import views

urlpatterns = [
    path('invoices', views.InvoiceGetAllAPIView.as_view(), name='invoice_list'),
    path('invoices/<int:pk>', views.InvoiceDetailAPIView.as_view(), name='invoice_detail'),
    path('invoices/create', views.InvoiceCreateAPIView.as_view(), name='invoice_create'),
    path('addresses', views.AddressGetAllAPIView.as_view(), name='address_list'),
    path('addresses/<int:pk>', views.AddressDetailAPIView.as_view(), name='address_detail'),
    path('addresses/create', views.AddressCreateAPIView.as_view(), name='address_create'),
    path('producers', views.ProducerGetAllAPIView.as_view(), name='producer_list'),
    path('producers/<int:pk>', views.ProducerDetailAPIView.as_view(), name='producer_detail'),
    path('producers/create', views.ProducerCreateAPIView.as_view(), name='producer_create'),
    path('medical_supplies', views.MedicalSupplyGetAllAPIView.as_view(), name='medical_supply_list'),
    path('medical_supplies/<int:pk>', views.MedicalSupplyDetailAPIView.as_view(), name='medical_supply_detail'),
    path('medical_supplies/create', views.MedicalSupplyCreateAPIView.as_view(), name='medical_supply_create'),
    path('invoice_details', views.InvoiceDetailGetAllAPIView.as_view(), name='invoice_detail_list'),
    path('invoice_details/<int:pk>', views.InvoiceDetailDetailAPIView.as_view(), name='invoice_detail_detail'),
    path('invoice_details/create', views.InvoiceDetailCreateAPIView.as_view(), name='invoice_detail_create'),
]
