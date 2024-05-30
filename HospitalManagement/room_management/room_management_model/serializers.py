from rest_framework import serializers
from .models import Clinic, HospitalRoom, Bed, Department

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class ClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = '__all__'

class HospitalRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalRoom
        fields = '__all__'

class BedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bed
        fields = '__all__'