from django.shortcuts import render
from PuzzModel.models import Storytable, Usertable


def homepage(request):
    story_list = Storytable.objects.order_by('-likescount')[:5]
    user_list = Usertable.objects.order_by('-experience')[:5]

    index_dict = {
        'display': 'homepage',
        'story_list': story_list,
        'user_list': user_list
    }

    # TODO: database search : ranking & trending
    # save into (key : list)
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
