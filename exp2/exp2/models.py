# !/usr/bin/python
# -*- coding: UTF-8 -*-

from django.db import models

class User(models.Model):
    sid = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=50)
    position = models.CharField(max_length=2, default="3") # 1:admin 2:teacher 3:student