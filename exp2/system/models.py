from django.db import models

# Create your models here.

class User(models.Model):
    sid = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=50)
    position = models.CharField(max_length=2, default="3") # 1:admin 2:teacher 3:student


class Student(models.Model):
    sid = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=50)
    grade = models.CharField(max_length=50)
    id = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    cls_name = models.CharField(max_length=50)

class Teacher(models.Model):
    tid = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=50)
    id = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

class Administrators(models.Model):
    aid = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=50)

class Course(models.Model):
    cid = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50)
    tid = models.CharField(max_length=50)

class Select_Course(models.Model):
    cid = models.CharField(max_length=50)
    sid = models.CharField(max_length=50)
    tid = models.CharField(max_length=50)

