from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Clinic, Room, Bed, Department, PatientBed
from .serializers import ClinicSerializer, RoomSerializer, BedSerializer, DepartmentSerializer, PatientBedSerializer

class DepartmentListCreate(APIView):
    def get(self, request):
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DepartmentDetail(APIView):
    def get(self, request, pk):
        department = Department.objects.get(pk=pk)
        serializer = DepartmentSerializer(department)
        return Response(serializer.data)
    
    def put(self, request, pk):
        department = Department.objects.get(pk=pk)
        serializer = DepartmentSerializer(department, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        department = Department.objects.get(pk=pk)
        department.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ClinicListCreate(APIView):
    def get(self, request):
        clinics = Clinic.objects.all()
        serializer = ClinicSerializer(clinics, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ClinicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClinicDetail(APIView):
    def get(self, request, pk):
        clinic = Clinic.objects.get(pk=pk)
        serializer = ClinicSerializer(clinic)
        return Response(serializer.data)
    
    def put(self, request, pk):
        clinic = Clinic.objects.get(pk=pk)
        serializer = ClinicSerializer(clinic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        clinic = Clinic.objects.get(pk=pk)
        clinic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ClinicByDepartment(APIView):
    def get(self, request, department_id):
        clinics = Clinic.objects.filter(department_id=department_id)
        serializer = ClinicSerializer(clinics, many=True)
        return Response(serializer.data)

class HospitalRoomListCreate(APIView):
    def get(self, request):
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HospitalRoomDetail(APIView):
    def get(self, request, pk):
        room = Room.objects.get(pk=pk)
        serializer = RoomSerializer(room)
        return Response(serializer.data)
    
    def put(self, request, pk):
        room = Room.objects.get(pk=pk)
        serializer = RoomSerializer(room, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        room = Room.objects.get(pk=pk)
        room.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class HospitalRoomByDepartment(APIView):
    def get(self, request, department_id):
        rooms = Room.objects.filter(department_id=department_id)
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)

class BedListCreate(APIView):
    def get(self, request):
        beds = Bed.objects.all()
        serializer = BedSerializer(beds, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BedDetail(APIView):
    def get(self, request, pk):
        bed = Bed.objects.get(pk=pk)
        serializer = BedSerializer(bed)
        return Response(serializer.data)
    
    def put(self, request, pk):
        bed = Bed.objects.get(pk=pk)
        serializer = BedSerializer(bed, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        bed = Bed.objects.get(pk=pk)
        bed.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BedByRoom(APIView):
    def get(self, request, room_id):
        beds = Bed.objects.filter(room_id=room_id)
        serializer = BedSerializer(beds, many=True)
        return Response(serializer.data)

class PatientBedListCreate(APIView):
    def get(self, request):
        patient_beds = PatientBed.objects.all()
        serializer = PatientBedSerializer(patient_beds, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PatientBedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PatientBedDetail(APIView):
    def get(self, request, pk):
        patient_bed = PatientBed.objects.get(patient_id=pk)
        serializer = PatientBedSerializer(patient_bed)
        return Response(serializer.data)
    
    def put(self, request, pk):
        patient_bed = PatientBed.objects.get(pk=pk)
        serializer = PatientBedSerializer(patient_bed, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        patient_bed = PatientBed.objects.get(pk=pk)
        patient_bed.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)