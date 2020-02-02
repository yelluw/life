from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import localtime


class Exercise(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Activity(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.PROTECT)
    date_created = models.DateTimeField()
    duration = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.exercise.name
    class Meta:
        ordering = ['-date_created']
