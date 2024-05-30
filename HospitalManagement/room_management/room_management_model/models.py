from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=255)

class Clinic(models.Model):
    name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, related_name='clinics', on_delete=models.CASCADE)

class HospitalRoom(models.Model):
    number = models.CharField(max_length=50)
    department = models.ForeignKey(Department, related_name='hospital_rooms', on_delete=models.CASCADE)

class Bed(models.Model):
    number = models.CharField(max_length=50)
    hospital_room = models.ForeignKey(HospitalRoom, related_name='beds', on_delete=models.CASCADE)