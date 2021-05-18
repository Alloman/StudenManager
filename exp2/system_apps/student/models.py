from django.db import models

# Create your models here.

class Student(models.Model):
    sid = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=50)
    grade = models.CharField(max_length=50)
    id = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    cls_name = models.CharField(max_length=50)


    class Meta:
        db_table = "system_student"