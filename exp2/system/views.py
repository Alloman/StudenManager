from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User, Student, Teacher, Administrators, Course, Select_Course

# Create your views here.

# all user function
def login_view(request):

    if request.method == "GET" and not request.session.get("status", None):
        return render(request, "login.html")
    elif request.method == "GET":
        position = request.session['position']

        if position == '1':
            return render(request, "")
        elif position == '2':
            pass
        else:
            return render(request, "student_base.html")
    elif request.method == "POST":
        sid = request.POST['id']
        pwd = request.POST['password']

        try:
            db_user = User.objects.get(sid=sid)
            if db_user.password == pwd:
                request.session['status'] = True
                request.session['user_id'] = sid
                request.session['user_pwd'] = pwd
                request.session['position'] = db_user.position

                if db_user.position == '1':
                    return render(request, "")
                elif db_user.position == '2':
                    pass
                else:
                    return render(request, "student_base.html")
            else:
                message = "密码不正确"

        except:
            message = "用户不存在"

    return render(request, "login.html", locals())

def logout(request):
    if request.session.get("status", None):
        request.session.flush()

    return render(request, "../templates/index.html")



# student function
def select_course(request):

    cid = request.GET['cid']
    sid = request.session["user_id"]

    info = Course.objects.filter(cid=cid)[0]

    Select_Course.objects.create(cid=info.cid, sid=sid, tid=info.tid)

    sc_list = Select_Course.objects.filter(sid=sid)
    all_c = Course.objects.all()
    all_cid = []
    for sc in sc_list:
        all_cid.append(sc.cid)

    all_c_info = []
    for c in all_c:
        cid = c.cid
        cname = c.name
        tname = Teacher.objects.filter(tid=c.tid)[0].name

        all_c_info.append({
            "cid": cid,
            "cname": cname,
            "tname": tname
        })

    return render(request, "student_select.html", locals())


def find_no_select_course(request):
    sid = request.session["user_id"]

    sc_list = Select_Course.objects.filter(sid=sid)
    all_c = Course.objects.all()
    all_cid = []
    for sc in sc_list:
        all_cid.append(sc.cid)

    all_c_info = []
    for c in all_c:
        cid = c.cid
        cname = c.name
        tname = Teacher.objects.filter(tid=c.tid)[0].name

        all_c_info.append({
            "cid" : cid,
            "cname" : cname,
            "tname" : tname
        })

    return render(request, "student_select.html", locals())

def del_select_course(request):

    cid = request.GET['cid']
    sid = request.session["user_id"]

    sc = Select_Course.objects.filter(cid=cid, sid=sid)
    sc.delete()

    all_info = []
    sc_list = Select_Course.objects.filter(sid=sid)
    for sc in sc_list:
        course_info = Course.objects.filter(cid=sc.cid)[0]
        teacher_info = Teacher.objects.filter(tid=sc.tid)[0]
        all_info.append({"course_info": course_info,
                         "teacher_info": teacher_info,
                         })
    return render(request, "student_find.html", locals())


def find_select_course(request):
    sid = request.session["user_id"]

    sc_list = Select_Course.objects.filter(sid=sid)
    all_info = []

    for sc in sc_list:
        course_info = Course.objects.filter(cid=sc.cid)[0]
        teacher_info = Teacher.objects.filter(tid=sc.tid)[0]
        all_info.append({"course_info": course_info,
                         "teacher_info": teacher_info,
                         })
    return render(request, "student_find.html", locals())


# teacher function
def find_teach_student(request):
    pass

def find_teach_course(request):
    pass

def add_teach_course(request):
    pass

def del_teach_course(request):
    pass


# admin function
def add_student(request):
    pass

def del_student(request):
    pass

def find_student(request):
    pass

def add_course(request):
    pass

def del_course(request):
    pass

def find_course(request):
    pass


