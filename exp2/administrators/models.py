from django.db import models

# Create your models here.

class Administrators(models.Model):
    sid = models.CharField(max_length=50)
    name = models.CharField(max_length=50)