from rest_framework import serializers
from .models import ServiceInvoice, MedicationInvoice

class ServiceInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceInvoice
        fields = '__all__'

class MedicationInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicationInvoice
        fields = '__all__'