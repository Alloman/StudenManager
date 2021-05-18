from django.shortcuts import render
from ..course.models import Course, Select_Course
from ..teacher.models import Teacher


# Create your views here.

def student_index(request):
    sid = request.session['user_id']

    return render(request, "student_base.html", locals())

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
        ccredit = c.credit
        tname = Teacher.objects.filter(tid=c.tid)[0].name

        all_c_info.append({
            "cid": cid,
            "cname": cname,
            "ccredit": ccredit,
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
        ccredit= c.credit
        tname = Teacher.objects.filter(tid=c.tid)[0].name

        all_c_info.append({
            "cid" : cid,
            "cname" : cname,
            "ccredit" : ccredit,
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
                         "grade": sc.grade,
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
                         "grade" : sc.grade,
                         })
    return render(request, "student_find.html", locals())
