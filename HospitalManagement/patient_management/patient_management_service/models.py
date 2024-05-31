from django.db import models

class FullName(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    class Meta:
        db_table = 'full_names'
class Address(models.Model):
    id = models.AutoField(primary_key=True)
    no_house = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    class Meta:
        db_table = 'address'
class Account(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, null=False, unique=True)
    password = models.CharField(max_length=255, null=False)
    class Meta:
        db_table = 'accounts'
class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.ForeignKey(FullName, null=False, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    is_active = models.IntegerField(default=1)
    class Meta:
        db_table = 'patients'