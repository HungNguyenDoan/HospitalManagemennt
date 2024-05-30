from rest_framework import serializers
from .models import *

class PharmacySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacy
        fields = ['id','name','description', 'price','madeIn']
