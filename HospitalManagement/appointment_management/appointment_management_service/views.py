from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Appointment
from .serializers import AppointmentSerializer
from django.utils.dateparse import parse_date
from django.shortcuts import get_object_or_404

class AppointmentList(APIView):
    def post(self, request):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        role = request.query_params.get('role')
        entity_id = request.query_params.get('id')
        date = request.query_params.get('date')

        if role and entity_id:
            if role.lower() == 'doctor':
                appointments = Appointment.objects.filter(doctorId=entity_id)
            elif role.lower() == 'patient':
                appointments = Appointment.objects.filter(patientId=entity_id)
            else:
                return Response({"detail": "Invalid role provided"}, status=status.HTTP_400_BAD_REQUEST)
            
            if date:
                parsed_date = parse_date(date)
                if parsed_date:
                    appointments = appointments.filter(appointmentDate=parsed_date)
                else:
                    return Response({"detail": "Invalid date format"}, status=status.HTTP_400_BAD_REQUEST)

            serializer = AppointmentSerializer(appointments, many=True)
            return Response(serializer.data)
        
        return Response({"detail": "Role and id are required parameters"}, status=status.HTTP_400_BAD_REQUEST)

class AppointmentDetail(APIView):
    def get_object(self, id):
        return get_object_or_404(Appointment, id=id)

    def get(self, request, id):
        appointment = self.get_object(id)
        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data)

    def put(self, request, id):
        appointment = self.get_object(id)
        serializer = AppointmentSerializer(appointment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        appointment = self.get_object(id)
        appointment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
