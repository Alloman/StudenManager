from django.shortcuts import render, redirect
from ..student.models import Student
from ..course.models import Course, Select_Course
from ..teacher.models import Teacher
from django.http import HttpResponse

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
        cid = info.cid
        cname = Course.objects.get(cid=info.cid).name
        sid = info.sid
        sname = Student.objects.get(sid=info.sid).name
        tname = Teacher.objects.get(tid=info.tid).name
        credit = Course.objects.get(cid=info.cid).credit
        grade  = info.grade

        info_list.append({
            "cid" : cid,
            "cname" : cname,
            "sid" : sid,
            "sname" : sname,
            "tname" : tname,
            "credit" : credit,
            "grade" : grade,
        })

    return render(request, "admin_grade.html", locals())

def alter_grade(request):
    if request.session["position"] != "1":
        return HttpResponse("<h1>无权限</h1>")

    cid = request.POST['cid']
    sid = request.POST['sid']
    grade = request.POST['grade']
    ret = {'status': True, 'message': None}

    if grade == "-1":
        grade = "-1"
        s_g = Select_Course.objects.get(cid=cid, sid=sid)
        s_g.grade = grade
        s_g.save()
    elif int(grade) > -1 and int(grade) < 101:
        s_g = Select_Course.objects.get(cid=cid, sid=sid)
        s_g.grade = grade
        s_g.save()
    else:
        ret['status'] = False
        ret['message'] = '处理异常'
        return HttpResponse("<h1>非法成绩！！</h1>")

    import json
    return HttpResponse(json.dumps(ret))
