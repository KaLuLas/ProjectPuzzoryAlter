from django.shortcuts import render


def homepage(request):
    index_dict = {
        'homepage': True,
        'upload_story': False,
        'system_message': False
    }
    return render(request, 'index.html', index_dict)


def upload_story(request):
    index_dict = {
        'homepage': False,
        'upload_story': True,
        'system_message': False
    }
    return render(request, 'index.html', index_dict)


def system_message(request):
    index_dict = {
        'homepage': False,
        'upload_story': False,
        'system_message': True
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
