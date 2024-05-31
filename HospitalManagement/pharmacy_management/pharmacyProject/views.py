from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import AddressSerializer, ProducerSerializer, MedicalSupplySerializer, InvoiceSerializer, InvoiceDetailSerializer
from .models import Address, Producer, MedicalSupply, Invoice, InvoiceDetail

class InvoiceGetAllAPIView(APIView):
    def get(self, request):
        all_invoices = Invoice.objects.all()
        serializers = InvoiceSerializer(all_invoices, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

class InvoiceDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            invoice = Invoice.objects.get(pk=pk)
        except Invoice.DoesNotExist:
            return Response({"error": "Invoice not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = InvoiceSerializer(invoice)
        return Response(serializer.data, status=status.HTTP_200_OK)

class InvoiceCreateAPIView(APIView):
    def post(self, request):
        serializer = InvoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddressGetAllAPIView(APIView):
    def get(self, request):
        all_addresses = Address.objects.all()
        serializers = AddressSerializer(all_addresses, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

class AddressDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            address = Address.objects.get(pk=pk)
        except Address.DoesNotExist:
            return Response({"error": "Address not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = AddressSerializer(address)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AddressCreateAPIView(APIView):
    def post(self, request):
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProducerGetAllAPIView(APIView):
    def get(self, request):
        all_producers = Producer.objects.all()
        serializers = ProducerSerializer(all_producers, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

class ProducerDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            producer = Producer.objects.get(pk=pk)
        except Producer.DoesNotExist:
            return Response({"error": "Producer not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProducerSerializer(producer)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ProducerCreateAPIView(APIView):
    def post(self, request):
        serializer = ProducerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MedicalSupplyGetAllAPIView(APIView):
    def get(self, request):
        all_medical_supplies = MedicalSupply.objects.all()
        serializers = MedicalSupplySerializer(all_medical_supplies, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

class MedicalSupplyDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            medical_supply = MedicalSupply.objects.get(pk=pk)
        except MedicalSupply.DoesNotExist:
            return Response({"error": "Medical Supply not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = MedicalSupplySerializer(medical_supply)
        return Response(serializer.data, status=status.HTTP_200_OK)

class MedicalSupplyCreateAPIView(APIView):
    def post(self, request):
        serializer = MedicalSupplySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InvoiceDetailGetAllAPIView(APIView):
    def get(self, request):
        all_invoice_details = InvoiceDetail.objects.all()
        serializers = InvoiceDetailSerializer(all_invoice_details, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

class InvoiceDetailDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            invoice_detail = InvoiceDetail.objects.get(pk=pk)
        except InvoiceDetail.DoesNotExist:
            return Response({"error": "Invoice Detail not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = InvoiceDetailSerializer(invoice_detail)
        return Response(serializer.data, status=status.HTTP_200_OK)

class InvoiceDetailCreateAPIView(APIView):
    def post(self, request):
        serializer = InvoiceDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
