from django.db import models

class Pharmacy(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    madeIn = models.TextField()
    def __str__(self):
        return self.name


# hóa đơn
class Invoice(models.Model):
    invoice_number = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    customer_name = models.CharField(max_length=200)
    customer_email = models.EmailField()
    def __str__(self):
        return self.invoice_number

