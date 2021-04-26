# !/usr/bin/python
# -*- coding: UTF-8 -*-

from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("hello world!")

