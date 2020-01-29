from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import localtime


class Todo(models.Model):
    task = models.CharField(max_length=255)
    notes = models.TextField(default='')
    date_created = models.DateTimeField(auto_now_add=True)
    date_due = models.DateTimeField()
    done = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.task} - Due: {localtime(self.date_due)}'

    class Meta:
        ordering = ['-id']

