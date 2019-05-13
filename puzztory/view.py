from django.shortcuts import render
from PuzzModel.models import Storytable, Usertable, Fragmenttable
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

index_dict = {
        'display': 'homepage',
        'story_list': '',
        'user_list': ''
    }


def homepage(request):
    # story_list = Storytable.objects.order_by('-likescount')[:5]
    # user_list = Usertable.objects.order_by('-experience')[:5]

    index_dict['display'] = 'homepage'
    index_dict['story_list'] = Storytable.objects.order_by('-likescount')[:5]
    index_dict['user_list'] = Usertable.objects.order_by('-experience')[:5]

    return render(request, 'index.html', index_dict)


def upload_story_page(request):
    index_dict['display'] = 'upload_story'
    return render(request, 'index.html', index_dict)


def upload_story(request):
    # keys in request.POST:
    # MUST HAVE: title, firstPart
    # MAY HAVE: branch, modified, ending -> 'on' if checkbox was checked
    # MAY HAVE: fragWordCount: the maximum number of words a fragment can have in current story
    # MAY HAVE: fragNumCount: the maximum number of fragments a story can have
    if request.method == 'POST':
        story_title = request.POST['title']
        first_frag_text = request.POST['firstPart']
        frag_record = Fragmenttable(
            content=first_frag_text, username=User.last_name, 
            useremail=User.username, storyid=0, branchid=0)
        frag_record.save()
        story_record = Storytable(
            username=User.last_name, useremail=User.username,
            title=story_title, beginning=frag_record.fragmentid, 
            fragmentscount=1
        )
        if request.POST.has_key('branch'):
            story_record.branch = '1'
        if not request.POST.has_key('modified'):
            story_record.branch = '0'
        if request.POST.has_key('ending'):
            story_record.finished = '1'
        if request.POST.has_key('fragWordCount'):
            story_record.wordslimit = '1'
            story_record.fragmentwordslimit = request.POST['fragWordCount']
        if request.POST.has_key('fragNumCount'):
            story_record.fragmentcapacity = request.POST['fragNumCount']
        story_record.save()
        frag_record.storyid = story_record.storyid
        frag_record.save()

    return HttpResponseRedirect("/")


def system_message(request):
    index_dict['display'] = 'system_message'
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
