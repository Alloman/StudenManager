from django.shortcuts import render, redirect
from ..student.models import Student
from ..course.models import Course, Select_Course
from ..teacher.models import Teacher

# Create your views here.

# student funcsion
def find_student(request):
    stu_list = Student.objects.all()

    return render(request, "admin_student.html", locals())

def add_student(request):
    pass

def alter_student(request):
    pass

def del_student(request):
    pass



# teacher funcsion
def find_teacher(request):
    tea_list = Teacher.objects.all()
    return render(request, "admin_teacher.html", locals())

def add_teacher(request):
    pass

def alter_teacher(request):
    pass

def del_teacher(request):
    pass



# course funcsion
def find_course(request):
    course_list = Course.objects.all()

    return render(request, "admin_course.html", locals())

def add_course(request):
    pass

def alter_course(request):
    pass

def del_course(request):
    pass



# grade funcsion
def find_grade(request):
    course_list = Course.objects.all()
    info_list = []

    

    return render(request, "admin_course.html", locals())

def alter_grade(request):
    pass

def del_grade(request):
    pass