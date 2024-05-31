from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import check_password

class FullNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = FullName
        fields = ['id','first_name', 'last_name']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id','no_house', 'street', 'city', 'country']

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'username', 'password']
    

class PatientInfoSerializer(serializers.ModelSerializer):
    full_name = FullNameSerializer()
    address = AddressSerializer()

    class Meta:
        model = Patient
        fields = ['id', 'full_name', 'address', 'date_of_birth','gender', 'phone_number', 'email']

class PatientLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True) 

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)

        if not username or not password:
            raise serializers.ValidationError('Username and password are required.')

        account = Account.objects.filter(username=username).first()
        if account:
            if check_password(password, account.password):
                patient = Patient.objects.filter(account=account.id).first()
                patient_serializer = PatientInfoSerializer(patient)
                return patient_serializer.data
            else:
                raise serializers.ValidationError('Invalid password.')
        else:
            raise serializers.ValidationError('Patient does not exist.')

class PatientUpdateInfoSerializer(serializers.ModelSerializer):
    full_name = FullNameSerializer(read_only=True)
    address = AddressSerializer(read_only=True)

    class Meta:
        model = Patient
        fields = ['id', 'full_name', 'address','date_of_birth','gender', 'phone_number', 'email']

class PatientSerializer(serializers.ModelSerializer):
    account = AccountSerializer()
    full_name = FullNameSerializer()
    address = AddressSerializer()

    class Meta:
        model = Patient
        fields = ['id','account', 'full_name', 'address','date_of_birth', 'phone_number', 'gender','email']

    def create(self, validated_data):
        account_data = validated_data.pop('account')
        full_name_data = validated_data.pop('full_name')
        address_data = validated_data.pop('address')

        account = Account.objects.create(**account_data)
        full_name = FullName.objects.create(**full_name_data)
        address = Address.objects.create(**address_data)

        patient = Patient.objects.create(
            account=account,
            full_name=full_name,
            address=address,
            phone_number=validated_data['phone_number'],
            gender=validated_data['gender'],
            date_of_birth=validated_data['date_of_birth'],
            email=validated_data['email']
        )
        return patient

    def update(self, instance, validated_data):
        pass
