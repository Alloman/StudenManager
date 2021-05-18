from django.shortcuts import render, redirect
from .models import User

# Create your views here.

def login_view(request):

    if request.method == "GET" and not request.session.get("status", None):
        return render(request, "login.html")
    elif request.method == "GET":
        position = request.session['position']

        if position == '1':
            return redirect("/system_admin")
        elif position == '2':
            return redirect("/teacher")
        else:
            return redirect("/student")
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

                if db_user.position == '1': # redirect可改变地址 数据由session保持
                    return redirect("/system_admin")
                elif db_user.position == '2':
                    return redirect("/teacher")
                    # return render(request, "teacher_base.html", locals())
                else:
                    return redirect("/student")
                    # return render(request, "student_base.html", locals())
            else:
                message = "密码不正确"

        except:
            message = "用户不存在"

    return render(request, "login.html", locals())

def logout(request):
    if request.session.get("status", None):
        request.session.flush()

    return redirect("/")