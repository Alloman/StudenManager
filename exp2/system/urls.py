# !/usr/bin/python
# -*- coding: UTF-8 -*-

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # all users urls
    path('login', views.login_view),
    path('logout', views.logout),

    # student urls
    path('select_course', views.select_course),
    path('find_no_select_course', views.find_no_select_course),
    path('del_select_course', views.del_select_course),
    path('find_select_course', views.find_select_course),

    # teacher urls
    path('find_student', views.find_student),
    path('find_teach_course', views.find_teach_course),
    path('add_teach_course', views.add_teach_course),
    path('del_teach_course', views.del_teach_course),

    # admin urls
    path('add_student', views.add_student),
    path('del_student', views.del_student),
    path('find_student', views.find_student),
    path('add_course', views.add_course),
    path('del_course', views.del_course),
    path('find_course', views.find_course),

]
