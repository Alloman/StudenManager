# !/usr/bin/python
# -*- coding: UTF-8 -*-

from django.http import HttpResponse
from django.shortcuts import render



def index_view(request):

    return render(request, 'index.html')

def login_view(request):

    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == "POST":
        print(request.POST['id'])
        print(request.POST['password'])
        return HttpResponse("<h1>登陆成功</h1>")
