from django.shortcuts import render, redirect
from ..student.models import Student
from ..course.models import Course, Select_Course
from ..teacher.models import Teacher

# Create your views here.

# public funcsion
def admin_index(request):
    sid = request.session["user_id"]

    return render(request, "admin_base.html", locals())

# student funcsion
def find_student(request):
    sid = request.session["user_id"]
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
    sid = request.session["user_id"]
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
    sid = request.session["user_id"]
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
    sid = request.session["user_id"]
    select_list = Select_Course.objects.all()
    info_list = []

    for info in select_list:
        cname = Course.objects.get(cid=info.cid).name
        sname = Student.objects.get(sid=info.sid).name
        tname = Teacher.objects.get(tid=info.tid).name
        credit = Course.objects.get(cid=info.cid).credit
        grade  = info.grade

        info_list.append({
            "cname" : cname,
            "sname" : sname,
            "tname" : tname,
            "credit" : credit,
            "grade" : grade,
        })

    return render(request, "admin_grade.html", locals())

def alter_grade(request):
    pass

def del_grade(request):
    pass