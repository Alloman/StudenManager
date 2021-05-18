# !/usr/bin/python
# -*- coding: UTF-8 -*-

from django.http import HttpResponse
from django.shortcuts import render



def index_view(request):

    return render(request, 'index.html')
