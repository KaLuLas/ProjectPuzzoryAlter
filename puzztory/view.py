from django.shortcuts import render


def homepage(request):
    index_dict = {
        'display': 'homepage'
    }
    return render(request, 'index.html', index_dict)


def upload_story(request):
    index_dict = {
        'display': 'upload_story'
    }
    return render(request, 'index.html', index_dict)


def system_message(request):
    index_dict = {
        'display': 'system_message'
    }
    return render(request, 'index.html', index_dict)


def login_page(request):
    login_dict = {
        'emailNotExistedAlert': "",
        'passwordIncorrect': "",
        'useremail': ""
    }
    return render(request, 'login.html', login_dict)


def register_page(request):
    register_dict = {
        'emailExistedAlert': ""
    }
    return render(request, 'register.html', register_dict)
