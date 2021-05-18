from django.db import models

# Create your models here.

class Course(models.Model):
    cid = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50)
    tid = models.CharField(max_length=50)
    credit = models.CharField(max_length=50)
    cls_name = models.CharField(max_length=50)


    class Meta:
        db_table = "system_course"

class Select_Course(models.Model):
    cid = models.CharField(max_length=50)
    sid = models.CharField(max_length=50)
    tid = models.CharField(max_length=50)
    grade = models.CharField(max_length=50, default='-1')


    class Meta:
        db_table = "system_select_course"
