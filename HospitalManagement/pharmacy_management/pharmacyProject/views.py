from django.shortcuts import render
from rest_framework import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *

from .models import *

class PharmacyGetAllAPIView(APIView):
    def get(self, request):
        all_pharmacies = Pharmacy.objects.all()
        serializers =  PharmacySerializer(all_pharmacies, many = True)
        return Response(serializers.data, status=status.HTTP_200_OK)

class PharmacyCreateAPIView(APIView):
    def post(self, request):
        serializer = PharmacySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PharmacyUpdateAPIView(APIView):
    def put(self, request, pk):
        try:
            pharmacy = Pharmacy.objects.get(pk=pk)
        except Pharmacy.DoesNotExist:
            return Response({"error": "Pharmacy not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = PharmacySerializer(pharmacy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PharmacyDeleteAPIView(APIView):
    def delete(self, request, pk):
        try:
            pharmacy = Pharmacy.objects.get(pk=pk)
        except Pharmacy.DoesNotExist:
            return Response({"error": "Pharmacy not found"}, status=status.HTTP_404_NOT_FOUND)

        pharmacy.delete()
        return Response({"message": "Pharmacy deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
