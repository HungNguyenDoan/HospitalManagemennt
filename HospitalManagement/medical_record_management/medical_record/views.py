from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MedicalRecord
from .serializer import MedicalRecordSerializer

class MedicalRecordAPIView(APIView):
    """
    A simple APIView for CRUD operations on MedicalRecord model.
    """

    def get(self, request):
        queryset = MedicalRecord.objects.all()
        serializer = MedicalRecordSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MedicalRecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        return get_object_or_404(MedicalRecord, pk=pk)

    def get(self, request, pk=None):
        medical_record = self.get_object(pk)
        serializer = MedicalRecordSerializer(medical_record)
        return Response(serializer.data)

    def put(self, request, pk=None):
        medical_record = self.get_object(pk)
        serializer = MedicalRecordSerializer(medical_record, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
