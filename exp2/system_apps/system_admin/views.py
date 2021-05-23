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
    if request.session["position"] != "1":
        return HttpResponse("<h1>无权限</h1>")
    sid = request.session["user_id"]
    stu_list = Student.objects.all()

    return render(request, "admin_student.html", locals())

def add_student(request):
    if request.session["position"] != "1":
        return HttpResponse("<h1>无权限</h1>")
    sid = request.POST["sid"]
    sname = request.POST["sname"]
    sex = request.POST["sex"]
    grade = request.POST["grade"]
    id = request.POST["id"]
    phone = request.POST["phone"]
    cls_name = request.POST["cls_name"]
    ret = {'status': True, 'message': None}

    if sex == "男":
        sex = "1"
    elif sex == "女":
        sex = "0"
    else:
        ret['status'] = False
        ret['message'] = '处理异常'
        return HttpResponse("<h1>非法性别！！</h1>")

    Student.objects.create(sid=sid, name=sname, sex=sex, grade=grade, id=id, phone=phone, cls_name=cls_name)

    import json
    return HttpResponse(json.dumps(ret))


def alter_student(request):
    if request.session["position"] != "1":
        return HttpResponse("<h1>无权限</h1>")
    # 获取信息
    sid = request.POST["sid"]
    sname = request.POST["sname"]
    sex = request.POST["sex"]
    grade = request.POST["grade"]
    id = request.POST["id"]
    phone = request.POST["phone"]
    cls_name = request.POST["cls_name"]
    ret = {'status': True, 'message': None}

    # 处理特殊信息
    if sex == "男":
        sex = "1"
    elif sex == "女":
        sex = "0"
    else:
        ret['status'] = False
        ret['message'] = '处理异常'
        return HttpResponse("<h1>非法性别！！</h1>")

    # 修改信息
    stu = Student.objects.get(sid=sid)

    stu.name = sname
    stu.sex = sex
    stu.grade = grade
    stu.id = id
    stu.phone = phone
    stu.cls_name = cls_name

    stu.save()

    import json
    return HttpResponse(json.dumps(ret))


def del_student(request):
    if request.session["position"] != "1":
        return HttpResponse("<h1>无权限</h1>")

    sid = request.GET['sid']
    stu = Student.objects.get(sid=sid)
    stu.delete()

    sid = request.session["user_id"]
    stu_list = Student.objects.all()

    return render(request, "admin_student.html", locals())



# teacher funcsion
def find_teacher(request):
    if request.session["position"] != "1":
        return HttpResponse("<h1>无权限</h1>")
    sid = request.session["user_id"]
    tea_list = Teacher.objects.all()

    return render(request, "admin_teacher.html", locals())

def add_teacher(request):
    if request.session["position"] != "1":
        return HttpResponse("<h1>无权限</h1>")
    tid = request.POST["tid"]
    tname = request.POST["tname"]
    sex = request.POST["sex"]
    id = request.POST["id"]
    phone = request.POST["phone"]
    ret = {'status': True, 'message': None}

    if sex == "男":
        sex = "1"
    elif sex == "女":
        sex = "0"
    else:
        ret['status'] = False
        ret['message'] = '处理异常'
        return HttpResponse("<h1>非法性别！！</h1>")

    Teacher.objects.create(tid=tid, name=tname, sex=sex, id=id, phone=phone)

    import json
    return HttpResponse(json.dumps(ret))

def alter_teacher(request):
    if request.session["position"] != "1":
        return HttpResponse("<h1>无权限</h1>")
    # 获取信息
    tid = request.POST["tid"]
    tname = request.POST["tname"]
    sex = request.POST["sex"]
    id = request.POST["id"]
    phone = request.POST["phone"]
    ret = {'status': True, 'message': None}

    # 处理特殊信息
    if sex == "男":
        sex = "1"
    elif sex == "女":
        sex = "0"
    else:
        ret['status'] = False
        ret['message'] = '处理异常'
        return HttpResponse("<h1>非法性别！！</h1>")

    # 修改信息
    tea = Teacher.objects.get(tid=tid)

    tea.name = tname
    tea.sex = sex
    tea.id = id
    tea.phone = phone

    tea.save()

    import json
    return HttpResponse(json.dumps(ret))

def del_teacher(request):
    if request.session["position"] != "1":
        return HttpResponse("<h1>无权限</h1>")

    print(request.GET)
    tid = request.GET['tid']
    tea = Teacher.objects.get(tid=tid)
    tea.delete()

    sid = request.session["user_id"]
    tea_list = Teacher.objects.all()

    return render(request, "admin_teacher.html", locals())



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
