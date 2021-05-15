# !/usr/bin/python
# -*- coding: UTF-8 -*-

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.stu_views)
]
