from django.shortcuts import render


def homepage(request):
    return render(request, 'index.html')


def login_page(request):
    login_dict = {}
    login_dict['emailNotExistedAlert'] = ""
    login_dict['passwordIncorrect'] = ""
    login_dict['useremail'] = ""
    return render(request, 'login.html', login_dict)


def register_page(request):
    register_dict = {}
    register_dict['emailExistedAlert'] = ""
    return render(request, 'register.html', register_dict)
