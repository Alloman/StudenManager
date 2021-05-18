from django.db import models

# Create your models here.

from django.db import models

class User(models.Model):
    sid = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=50)
    position = models.CharField(max_length=2, default="3")  # 1:system_admin 2:teacher 3:student


    class Meta:
        db_table = "system_user"