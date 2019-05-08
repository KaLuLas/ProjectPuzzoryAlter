# from django.http import HttpResponse
from PuzzModel.models import Usertable
# from django.shortcuts import render_to_response
# from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.db import IntegrityError


def register(request):
    login_dict = {
        'emailNotExistedAlert': "",
        'passwordIncorrect': "",
        'useremail': ""
    }
    request.encoding = 'utf-8'
    if request.method == 'POST':
        user_email = request.POST['e']
        user_name = request.POST['u']
        pwd = request.POST['p']
        # successfully create new user
        register_dict = {}
        try:
            user = User.objects.create_user(
                username=user_email, email=user_email, password=pwd)
        except IntegrityError:
            register_dict['emailExistedAlert'] = "邮箱地址已被注册"
            return render(request, 'register.html', register_dict)
        user.save()
        login_dict['useremail'] = user_email
        user_record = Usertable(useremail=user_email, username=user_name)
        user_record.save()
    return render(request, 'login.html', login_dict)


def Login(request):
    login_dict = {
        'emailNotExistedAlert': "",
        'passwordIncorrect': "",
        'useremail': ""
    }
    request.encoding = 'utf-8'
    if request.method == 'POST':
        user_email = request.POST['e']
        pwd = request.POST['p']
        try:
            Usertable.objects.get(useremail=user_email)
        except Usertable.DoesNotExist:
            login_dict['emailNotExistedAlert'] = "该用户不存在"
            return render(request, "login.html", login_dict)
        user = authenticate(username=user_email, password=pwd)
        if user is None:
            login_dict['passwordIncorrect'] = "密码错误"
            return render(request, "login.html", login_dict)
        else:
            login(request, user)
            return HttpResponseRedirect("/")
    return render(request, "login.html", login_dict)


def Logout(request):
    # End session
    logout(request)
    # return to homepage
    return HttpResponseRedirect("/")


def userpage(request, user_name):
    return HttpResponse("Sorry no userpage for you " + user_name + " yet")