from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def stu_views(request):
    return HttpResponse("<h1>stu page</h1>")