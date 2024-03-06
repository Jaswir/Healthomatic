from django.db import models

class PatientModel(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    birth_date = models.DateField()
    healthcard_number = models.CharField(max_length=100)
    appointment_timings = models.DateTimeField()
    age = models.IntegerField()

    priority = models.CharField(max_length=100)
    symptoms = models.TextField()
    diagnoses = models.TextField()


    def __str__(self):
        return self.name
