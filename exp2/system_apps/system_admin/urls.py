"""exp2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # student urls
    path("find_student", views.find_student),
    path("add_student", views.add_student),
    path("alter_student", views.alter_student),
    path("del_student", views.del_student),

    # teacher urls
    path("find_teacher", views.find_teacher),
    path("add_teacher", views.add_teacher),
    path("alter_teacher", views.alter_teacher),
    path("del_teacher", views.del_teacher),

    # course urls
    path("find_course", views.find_course),

    # grade urls
    path("find_grade", views.find_grade),
    path("alter_grade", views.alter_grade),

    # public urls
    path("", views.admin_index),
]
