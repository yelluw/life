from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import localtime

class Medication(models.Model):
    name = models.CharField(max_length=255)
    dosage = models.FloatField()
    measurement = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notes = models.TextField(default='')

    def __str__(self):
        return f'{self.name} - {self.dosage} {self.measurement}'

    class Meta:
        ordering = ['name']


class Usage(models.Model):
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
    taken = models.DateTimeField()
    note = models.TextField(default='')

    def __str__(self):
        return f'{localtime(self.taken)} - {self.medication.name} {self.medication.dosage} {self.medication.measurement}' 

    class Meta:
        ordering = ['-taken']
