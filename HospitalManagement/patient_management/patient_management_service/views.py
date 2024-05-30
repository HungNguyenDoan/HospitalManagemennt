from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from django.contrib.auth.hashers import make_password
from .models import *
from django.db import transaction
from django.http import Http404
from django.db.models import Q

class RegisterView(APIView):
    @transaction.atomic
    def post(self, request):
        patient_data = request.data
        username = patient_data.get('account', {}).get('username')
        check = Account.objects.filter(username=username).first()

        if check is not None:
            return Response({"message": "Tài khoản đã tồn tại"}, status=status.HTTP_400_BAD_REQUEST)

        patient_data['account']['password'] = make_password(patient_data['account'].get('password'))
        serializer = PatientSerializer(data=patient_data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        serializer = PatientLoginSerializer(data=request.data)
        if serializer.is_valid():
            patient = serializer.validated_data  
            patient_serializer = PatientInfoSerializer(patient)           
            return Response({
                'patient': patient_serializer.data,
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetAllPatient(APIView):
    def get(self, request):
        patients = Patient.objects.filter(is_active=1)
        serializers =  PatientInfoSerializer(patients, many = True)
        return Response(serializers.data, status=status.HTTP_200_OK)    
class GetPatientByDoctor(APIView):
    def get(self, request, doctor_id):
        health_records = HealthRecord.objects.filter(doctor_id=doctor_id)
        patients = []
        for health_record in health_records:
            patient = Patient.objects.filter(pk=health_record.patient.id, is_active=1).first()
            if patient not in patients and patient is not None:
                patients.append(patient)
        serializers = PatientInfoSerializer(patients, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)    
        
class GetPatientDetail(APIView):
    def get_object(self, id):
        try:
            return Patient.objects.get(pk=id)
        except Patient.DoesNotExist:
            return None
        
    def get(self, request,id):
        patient = self.get_object(id)
        if patient is None:
            return Response({"message":"Bệnh nhân không tồn tại"}, status=status.HTTP_404_NOT_FOUND)
        serializer = PatientInfoSerializer(patient)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UpdateInfoPatient(APIView):
    def get_object(self, id):
        try:
            return Patient.objects.get(pk=id)
        except Patient.DoesNotExist:
            return None
    @transaction.atomic
    def put(self, request, id):
        patient = self.get_object(id)
        if patient is None:
            return Response({"message":"Bệnh nhân không tồn tại"}, status=status.HTTP_404_NOT_FOUND)
        full_name_data = request.data.get('full_name', {})
        address_data = request.data.get('address', {})
        full_name_serializer = FullNameSerializer(patient.full_name, full_name_data)
        if full_name_serializer.is_valid():
            full_name_serializer.save()
        else:
            return Response(full_name_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        address_serializer = AddressSerializer(patient.address, address_data)
        if address_serializer.is_valid():
            address_serializer.save()
        else:
            return Response(address_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer = PatientUpdateInfoSerializer(patient, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class DeletePatient(APIView):
    def get_object(self, id):
        try:
            return Patient.objects.get(pk=id)
        except Patient.DoesNotExist:
            return None
    def delete(self, request, id):
        patient = self.get_object(id)
        if patient is None:
            return Response({"message":"Bệnh nhân không tồn tại"}, status=status.HTTP_404_NOT_FOUND)
        try:
            patient.is_active = 0
            patient.save()
            return Response({"message": "Bệnh nhân đã được xóa"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": f"Lỗi khi xóa bệnh nhân: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

class GetAllHealthRecord(APIView):
    def get(self, request):
        health_records = HealthRecord.objects.all()
        serializers = HealthDetailRecordSerializer(health_records, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
class GetHealthRecordPatient(APIView):
    def get(self, request, patient_id):
        health_records = HealthRecord.objects.filter(patient=patient_id)
        serializers = HealthDetailRecordSerializer(health_records, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK) 
    
class CreateHealthRecord(APIView):
    def post(self, request):
        serializer = HealthRecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class UpdateHealthRecord(APIView):
    def get_object(self, id):
        try:
            return HealthRecord.objects.get(pk=id)
        except HealthRecord.DoesNotExist:
            return None
    def put(self, request, health_record_id):
        health_record = self.get_object(health_record_id)
        if health_record is None:
            return Response({"message":"Báo cáo không tồn tại"}, status=status.HTTP_404_NOT_FOUND)
        serializer = HealthRecordSerializer(health_record, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteHealthRecord(APIView):
    def get_object(self, id):
        try:
            return HealthRecord.objects.get(pk=id)
        except HealthRecord.DoesNotExist:
            return None
    def delete(self, request, health_record_id):
        health_record = self.get_object(health_record_id)
        if health_record is None:
            return Response({"message":"Báo cáo không tồn tại"}, status=status.HTTP_404_NOT_FOUND)
        try:
            check = health_record.delete()
            if check:
                return Response({"message": "Báo cáo đã được xóa"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": f"Lỗi khi xóa báo cáo: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)


class SearchPatient(APIView):
    def get(self, request):
        keyword = request.query_params.get('keyword','')
        patients = []
        if keyword:
            if keyword.isdigit():
                id_keyword = int(keyword)
                patient_query = Patient.objects.filter(Q(id=id_keyword))
                if patient_query is not None:
                    patients.extend(patient_query)
            full_names = FullName.objects.all()
            for full_name in full_names:
                name = full_name.first_name+" "+ full_name.last_name
                if name.lower().find(keyword.lower()) != -1 or keyword.lower().find(name.lower()) != -1:
                    patient = Patient.objects.filter(full_name=full_name.id).first()
                    print(patient)
                    if patient not in patients:
                        patients.append(patient)        
            adress = Address.objects.all()
            for ar in adress:
                if keyword.lower().find(ar.no_house.lower()) != -1 or keyword.lower().find(ar.street.lower()) !=-1 or keyword.lower().find(ar.city.lower()) !=-1 or keyword.lower().find(ar.country.lower()) !=-1:
                    patient = Patient.objects.filter(address=ar.id).first()
                    if patient not in patients:
                        patients.append(patient)  
            health_records = HealthRecord.objects.all()
            for health_record in health_records:
                if health_record.diagnosis.lower().find(keyword.lower())!=-1 or health_record.description.lower().find(keyword.lower())!=-1:
                    patient = Patient.objects.filter(pk=health_record.patient.id).first()
                    if patient not in patients:
                        patients.append(patient)  
        serializers = PatientInfoSerializer(patients, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)