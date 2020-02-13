from django.db import models
from django.urls import reverse

# Create your models here.

class Playbook(models.Model):
    name = models.CharField(max_length=200)
    script = models.FileField(upload_to='',default='test.yml')
    details = models.CharField(max_length=200,null=True)

    def get_absolute_url(self):
        return reverse('ansible_web:home')

    def __str__(self):
        return self.name
