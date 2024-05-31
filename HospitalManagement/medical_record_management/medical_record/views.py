import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import MedicalRecord
from .serializer import MedicalRecordSerializer

class MedicalRecordAPIView(APIView):

    def get_patient_info(self, patient_id):
        url = f'http://127.0.0.1:8000/api/patient/{patient_id}/'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def get(self, request, pk=None):
        if pk is not None:
            medical_record = get_object_or_404(MedicalRecord, pk=pk)
            patient_info = self.get_patient_info(medical_record.patient_id)
            serializer = MedicalRecordSerializer(medical_record)
            data = serializer.data
            if patient_info:
                data['patient_info'] = patient_info
            data.pop('patient_id', None)
            return Response(data)
        else:
            queryset = MedicalRecord.objects.all()
            serializer = MedicalRecordSerializer(queryset, many=True)
            data_list = serializer.data
            for data in data_list:
                patient_info = self.get_patient_info(data['patient_id'])
                if patient_info:
                    data['patient_info'] = patient_info
                data.pop('patient_id', None)
            return Response(data_list)

    def post(self, request):
        serializer = MedicalRecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)