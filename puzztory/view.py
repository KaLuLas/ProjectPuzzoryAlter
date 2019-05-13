from django.shortcuts import render
from PuzzModel.models import Storytable, Usertable
from django.http import HttpResponse


def homepage(request):
    story_list = Storytable.objects.order_by('-likescount')[:5]
    user_list = Usertable.objects.order_by('-experience')[:5]

    index_dict = {
        'display': 'homepage',
        'story_list': story_list,
        'user_list': user_list
    }

    return render(request, 'index.html', index_dict)


def upload_story_page(request):
    story_list = Storytable.objects.order_by('-likescount')[:5]
    user_list = Usertable.objects.order_by('-experience')[:5]

    index_dict = {
        'display': 'upload_story',
        'story_list': story_list,
        'user_list': user_list
    }

    return render(request, 'index.html', index_dict)


def upload_story(request):
    str = ''
    if request.method == 'POST':
        for key, value in request.POST.items():
            str += (key + ' : ' + value)
    return HttpResponse(str)


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
