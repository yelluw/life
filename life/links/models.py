from django.db import models
from django.contrib.auth.models import User


class Link(models.Model):
    url = models.URLField(max_length=2048) # longest url allowed by search engines
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-title']

class LinkGroup(models.Model):
    name = models.CharField(max_length=255)
    links = models.ManyToManyField(Link)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']
