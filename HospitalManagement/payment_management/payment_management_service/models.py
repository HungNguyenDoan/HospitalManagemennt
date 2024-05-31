from django.db import models

#Hoa đơn dịch vụ
class ServiceInvoice(models.Model):
    id = models.AutoField(primary_key=True)
    patientId = models.PositiveIntegerField(null=True)
    patientName = models.CharField(max_length=40, null=True)
    service_date = models.DateField(auto_now_add=True)
    service_description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Service Invoice #{self.id} for {self.patient}"

#Hóa đơn thuốc
class MedicationInvoice(models.Model):
    id = models.AutoField(primary_key=True)
    patientId = models.PositiveIntegerField(null=True)
    patientName = models.CharField(max_length=40, null=True)
    prescription_date = models.DateField(auto_now_add=True)
    medication_list = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Medication Invoice #{self.id} for {self.patient}"