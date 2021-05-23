from django.shortcuts import render, redirect
from django.http import HttpResponse
from ..course.models import Select_Course, Course
from ..student.models import Student

# Create your views here.

# public function
def teacher_index(request):
    tid = request.session["user_id"]

    return render(request, "teacher_base.html", locals())

# submit function
def submit_grade(request):
    if request.session["position"] != "2":
        return HttpResponse("<h1>无权限</h1>")

    # print("submit successfully!!!!!!!!!")
    cid = request.POST['cid']
    sid = request.POST['sid']
    grade = request.POST['grade']
    ret = {'status': True, 'message': None}
    # print("post:", request.POST)
    # print("cid: ",cid)
    # print("sid: ",sid)
    # print("grade:", grade)

    if grade == "未给成绩":
        grade = "-1"
        s_g = Select_Course.objects.get(cid=cid, sid=sid)
        s_g.grade = grade
        s_g.save()
    elif int(grade) > -1 and int(grade) <101:
        s_g = Select_Course.objects.get(cid=cid, sid=sid)
        s_g.grade = grade
        s_g.save()
    else:
        ret['status'] = False
        ret['message'] = '处理异常'
        return HttpResponse("<h1>非法成绩！！</h1>")

    import json
    return HttpResponse(json.dumps(ret))


def find_no_grade_info(request):
    if request.session["position"] != "2":
        return HttpResponse("<h1>无权限</h1>")

    tid = request.session["user_id"]

    select_c_infos = Select_Course.objects.filter(tid=tid)

    no_grade_info_list = []
    for select_c_info in select_c_infos:

        if select_c_info.grade != "-1":
            # 跳过有成绩的学生课程信息
            continue

        cid = select_c_info.cid
        cname = Course.objects.get(cid=cid).name
        sid = select_c_info.sid
        sname = Student.objects.get(sid=sid).name
        credit  = Course.objects.get(cid=cid).credit
        grade = select_c_info.grade

        no_grade_info_list.append({
            "cid" : cid,
            "cname" : cname,
            "sid" : sid,
            "sname" : sname,
            "credit" : credit,
            "grade" : grade,
        })

    return render(request, "teacher_submit.html", locals())


# find info
def find_teach_student(request):
    if request.session["position"] != "2":
        return HttpResponse("<h1>无权限</h1>")

    tid = request.session["user_id"]

    select_c_infos = Select_Course.objects.filter(tid=tid)

    no_grade_info_list = []
    for select_c_info in select_c_infos:

        if select_c_info.grade == "-1":
            # 跳过有无成绩的学生课程信息
            continue

        cid = select_c_info.cid
        cname = Course.objects.get(cid=cid).name
        sid = select_c_info.sid
        sname = Student.objects.get(sid=sid).name
        credit = Course.objects.get(cid=cid).credit
        grade = select_c_info.grade

        no_grade_info_list.append({
            "cid": cid,
            "cname": cname,
            "sid": sid,
            "sname": sname,
            "credit": credit,
            "grade": grade,
        })

    return render(request, "teacher_find.html", locals())

def update_grade(request):
    if request.session["position"] != "2":
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
