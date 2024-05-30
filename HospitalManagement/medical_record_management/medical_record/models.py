from djongo import models

class MedicalTest(models.Model):
    name = models.CharField(max_length=255)

class MedicalRecord(models.Model):
    _id = models.ObjectIdField()
    patient_id = models.CharField(max_length=255)
    doctor_id = models.CharField(max_length=255)
    date = models.DateField()
    reason = models.CharField(max_length=255)
    symptoms = models.CharField(max_length=255)
    first_diagnosis = models.CharField(max_length=255)
    medical_tests = models.ArrayField(
        model_container=MedicalTest,
        default=list
    )
    final_diagnosis = models.CharField(max_length=255)
    treatment_plan = models.CharField(max_length=255)
    note = models.TextField()

    class Meta:
        db_table = 'medical_records'
