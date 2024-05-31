from django.db import models


# Create your models here.
class Address(models.Model):
    no = models.TextField(max_length=255)
    street = models.TextField(max_length=255)
    district = models.TextField(max_length=255)
    city = models.TextField(max_length=255)
    province = models.TextField(max_length=255)
    country = models.TextField(max_length=255)

    class Meta:
        db_table = "addresses"


class Producer(models.Model):
    name = models.TextField(max_length=255)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    class Meta:
        db_table = "producers"


class Category(models.Model):
    name = models.TextField(max_length=255)

    class Meta:
        db_table = "categories"


class MedicalSupply(models.Model):
    name = models.TextField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=255)
    note = models.TextField(max_length=255)

    class Meta:
        db_table = "medical_supplies"
