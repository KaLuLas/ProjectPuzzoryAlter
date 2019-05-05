# from django.http import HttpResponse
from PuzzModel.models import Usertable
# from django.shortcuts import render_to_response
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render


def register(request):
    login_dict = {
        'emailNotExistedAlert': "",
        'passwordIncorrect': "",
        'useremail': ""
    }
    request.encoding = 'utf-8'
    if request.method == 'POST':
        user_email = request.POST['e']
        email_query = Usertable.objects.filter(useremail=user_email)

        if(len(email_query) == 1):
            register_dict = {}
            register_dict['emailExistedAlert'] = "邮箱地址已被注册"
            return render(request, 'register.html', register_dict)

        # successfully create new user
        user_name = request.POST['u']
        pwd = request.POST['p']
        mpwd = make_password(pwd, None, 'pbkdf2_sha256')
        user_record = Usertable(useremail=user_email,
                                username=user_name, password=mpwd)
        user_record.save()
        login_dict['useremail'] = user_email
    return render(request, 'login.html', login_dict)


def login(request):
    login_dict = {
        'emailNotExistedAlert': "",
        'passwordIncorrect': "",
        'useremail': ""
    }
    request.encoding = 'utf-8'
    if request.method == 'POST':
        user_email = request.POST['e']
        pwd = request.POST['p']
        user_query = Usertable.objects.filter(useremail=user_email)
        # user not existed error
        if len(user_query) == 0:
            login_dict['emailNotExistedAlert'] = "该用户不存在"
            return render(request, "login.html", login_dict)
        # password unmatch error
        elif len(user_query) == 1 and not check_password(pwd, user_query[0].password):
            login_dict['passwordIncorrect'] = "密码错误"
            return render(request, "login.html", login_dict)
        else:
            return render(request, "index.html")
    return render(request, "login.html", login_dict)
