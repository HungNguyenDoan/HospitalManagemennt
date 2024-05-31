# billing/urls.py
from django.urls import path
from .views import (
    ServiceInvoiceCreateView, ServiceInvoiceDetailView, ServiceInvoiceUpdateView,
    MedicineInvoiceCreateView, MedicineInvoiceDetailView, MedicineInvoiceUpdateView,
    PaymentView
)

urlpatterns = [
    path('service-invoices/', ServiceInvoiceCreateView.as_view(), name='service-invoice-create'),
    path('service-invoices/<int:id>/', ServiceInvoiceDetailView.as_view(), name='service-invoice-detail'),
    path('service-invoices/<int:id>/update/', ServiceInvoiceUpdateView.as_view(), name='service-invoice-update'),
    path('medicine-invoices/', MedicineInvoiceCreateView.as_view(), name='medicine-invoice-create'),
    path('medicine-invoices/<int:id>/', MedicineInvoiceDetailView.as_view(), name='medicine-invoice-detail'),
    path('medicine-invoices/<int:id>/update/', MedicineInvoiceUpdateView.as_view(), name='medicine-invoice-update'),
    path('payment/<str:invoice_type>/<int:id>/', PaymentView.as_view(), name='payment'),
]
