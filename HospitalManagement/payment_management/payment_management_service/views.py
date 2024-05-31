# billing/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import ServiceInvoice, MedicineInvoice
from .serializers import ServiceInvoiceSerializer, MedicineInvoiceSerializer

# Service Invoice Views
class ServiceInvoiceCreateView(APIView):
    def post(self, request):
        serializer = ServiceInvoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ServiceInvoiceDetailView(APIView):
    def get(self, request, id):
        service_invoice = get_object_or_404(ServiceInvoice, id=id)
        serializer = ServiceInvoiceSerializer(service_invoice)
        return Response(serializer.data)

class ServiceInvoiceUpdateView(APIView):
    def put(self, request, id):
        service_invoice = get_object_or_404(ServiceInvoice, id=id)
        serializer = ServiceInvoiceSerializer(service_invoice, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Medicine Invoice Views
class MedicineInvoiceCreateView(APIView):
    def post(self, request):
        serializer = MedicineInvoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MedicineInvoiceDetailView(APIView):
    def get(self, request, id):
        medicine_invoice = get_object_or_404(MedicineInvoice, id=id)
        serializer = MedicineInvoiceSerializer(medicine_invoice)
        return Response(serializer.data)

class MedicineInvoiceUpdateView(APIView):
    def put(self, request, id):
        medicine_invoice = get_object_or_404(MedicineInvoice, id=id)
        serializer = MedicineInvoiceSerializer(medicine_invoice, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Payment Processing View
class PaymentView(APIView):
    def post(self, request, invoice_type, id):
        if invoice_type == 'service':
            invoice = get_object_or_404(ServiceInvoice, id=id)
        elif invoice_type == 'medicine':
            invoice = get_object_or_404(MedicineInvoice, id=id)
        else:
            return Response({'error': 'Invalid invoice type'}, status=status.HTTP_400_BAD_REQUEST)

        # Implement payment processing logic here

        return Response({'message': 'Payment processed successfully'}, status=status.HTTP_200_OK)
