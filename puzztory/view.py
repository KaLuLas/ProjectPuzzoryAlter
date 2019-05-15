from django.shortcuts import render
# from PuzzModel.models import Storytable, Fragmenttable
# from PuzzModel.models import UserExtension

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse

index_dict = {
        'display': 'homepage',
        'story_list': '',
        'user_list': '',
        'story_full_list': ''
    }


def homepage(request):
    # story_list = Storytable.objects.order_by('-likescount')[:5]
    # user_list = Usertable.objects.order_by('-experience')[:5]

    index_dict['display'] = 'homepage'
    # index_dict['story_list'] = Storytable.objects.order_by('-likescount')[:5]
    # index_dict['user_list'] = Usertable.objects.order_by('-experience')[:5]
    # TODO: FUCK add content of the first fragment into the dictionary
    # index_dict['story_full_list'] = Storytable.objects.order_by('-createtime')

    return render(request, 'index.html', index_dict)


def storypage(request, story_id):
    story_dict = {
        #'story': Storytable.objects.get(storyid=story_id)
     }
    # story_dict['story'] = Storytable.objects.get(storyid=story_id)
    # return HttpResponse("You're looking at story %s." % story_id)
    return render(request, 'story.html', story_dict)


def upload_story_page(request):
    index_dict['display'] = 'upload_story'
    #index_dict['story_list'] = Storytable.objects.order_by('-likescount')[:5]
    #index_dict['user_list'] = Usertable.objects.order_by('-experience')[:5]

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
            content=first_frag_text, username=request.user.last_name,
            useremail=request.user.username, storyid=0, branchid=0)
        frag_record.save()
        # story_record = Storytable(
        #     username=request.user.last_name, useremail=request.user.username,
        #     title=story_title, beginning=frag_record.fragmentid,
        #     fragmentscount=1
        # )
        if 'branch' in request.POST:
            story_record.branch = '1'
        if 'modified' not in request.POST:
            story_record.modified = '0'
        # if 'ending' in request.POST:
            # TODO: need another attribute
            # story_record.finished = '1'
            # pass
        if 'fragWordCount' in request.POST:
            story_record.wordslimit = '1'
            story_record.fragmentwordslimit = request.POST['fragWordCount']
        if 'fragNumCount' in request.POST:
            story_record.fragmentcapacity = request.POST['fragNumCount']
        story_record.save()
        frag_record.storyid = story_record.storyid
        frag_record.save()

    return HttpResponseRedirect("/")


def system_message(request):
    index_dict['display'] = 'system_message'
    # index_dict['story_list'] = Storytable.objects.order_by('-likescount')[:5]
    # index_dict['user_list'] = Usertable.objects.order_by('-experience')[:5]

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
