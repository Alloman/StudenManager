from django.db import models

# Create your models here.

class Administrators(models.Model):
    aid = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=50)


    class Meta:
        db_table = "system_Administrators"