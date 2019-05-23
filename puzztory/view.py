from django.shortcuts import render
from PuzzModel.models import Story, Fragment, UserExtension
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core.paginator import Paginator
import time

index_dict = {
        'display': 'homepage',
        'story_list': '',
        'user_list': ''
    }

# seconds
submit_countdown = 30


def homepage(request):
    index_dict['display'] = 'homepage'
    index_dict['story_list'] = Story.objects.order_by('-likescount')[:5]
    index_dict['user_list'] = UserExtension.objects.order_by('-experience')[:5]
    
    # for Pagination
    story_full_list = Story.objects.order_by('-createtime')
    paginator = Paginator(story_full_list, 10)
    # if request.method == 'GET':
    page = request.GET.get('page')
    if page == None:
        page = 1
    page_obj = paginator.get_page(page)
    index_dict['paginator'] = paginator
    index_dict['page_obj'] = page_obj
    if(paginator.num_pages > 1):
        is_paginated = True
    else:
        is_paginated = False
    index_dict['is_paginated'] = is_paginated
    return render(request, 'index.html', index_dict)


def storypage(request, story_id):
    frag_full_list = Fragment.objects.filter(storyid=story_id).order_by('createtime')
    paginator = Paginator(frag_full_list,7)
    # if request.method == 'GET':
    page = request.GET.get('page')
    if page == None:
        page = 1
    
    page_obj = paginator.page(page)
    if(paginator.num_pages > 1):
        is_paginated = True
    else:
        is_paginated = False
    story_dict = {
        'story': Story.objects.get(id=story_id),
        'paginator': paginator,
        'page_obj': page_obj,
        'is_paginated': is_paginated
     }
    return render(request, 'story.html', story_dict)


def upload_story_page(request):
    index_dict['display'] = 'upload_story'
    index_dict['story_list'] = Story.objects.order_by('-likescount')[:5]
    index_dict['user_list'] = UserExtension.objects.order_by('-experience')[:5]
    return render(request, 'index.html', index_dict)


def upload_frag(request, story_id):
    if request.method == 'POST':
        frag_text = request.POST['fcontent']
        frag_record = Fragment(
            content=frag_text, nickname=request.user.userextension.nickname,
            email=request.user.email, storyid=story_id)
        frag_record.save()
        story_record = Story.objects.get(id=story_id)
        story_record.fragscount += 1
        # unlock the story once the fragment is submitted
        story_record.lock = False
        story_record.save()
        current_user = UserExtension.objects.get(id=request.user.id)
        current_user.experience += 2
        current_user.save()

    frag_full_list = Fragment.objects.filter(storyid=story_id).order_by('createtime')
    paginator = Paginator(frag_full_list,7)
    return HttpResponseRedirect("/story/" + str(story_id) + "?page=" + str(paginator.num_pages))


def upload_story(request):
    # keys in request.POST:
    # MUST HAVE: title, ffcontent
    # MAY HAVE: branch, modified -> 'on' if checkbox was checked
    # MAY HAVE: fragWordsLimit: the maximum number of words a fragment can have in current story
    # MAY HAVE: fragsCountLimit: the maximum number of fragments a story can have
    if request.method == 'POST':
        story_title = request.POST['title']
        first_frag_text = request.POST['ffcontent']
        frag_record = Fragment(
            content=first_frag_text, nickname=request.user.userextension.nickname,
            email=request.user.email, storyid=0)
        frag_record.save()
        story_record = Story(
            nickname=request.user.userextension.nickname, email=request.user.email,
            title=story_title, ffid=frag_record.id, ffcontent=first_frag_text)

        if 'branch' in request.POST:
            story_record.branch = True
        if 'modified' not in request.POST:
            story_record.modified = False
        if 'fragWordsLimit' in request.POST:
            story_record.fragwordslimit = request.POST['fragWordsLimit']
        if 'fragsCountLimit' in request.POST:
            story_record.fragscountlimit = request.POST['fragsCountLimit']
        story_record.save()
        frag_record.storyid = story_record.id
        frag_record.save()
        current_user = UserExtension.objects.get(id=request.user.id)
        current_user.experience += 10
        current_user.save()

    return HttpResponseRedirect("/")


def system_message(request):
    index_dict['display'] = 'system_message'
    index_dict['story_list'] = Story.objects.order_by('-likescount')[:5]
    index_dict['user_list'] = UserExtension.objects.order_by('-experience')[:5]
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


def lock(request):
    request_id = request.GET.get('story_id')
    story = Story.objects.get(id=request_id)
    ret_dict = {}
    if not story.lock:
        story.lock = True
        story.save()
        ret_dict['lock'] = False
        ret_dict['submitcountdown'] = submit_countdown
        last_fragment = Fragment.objects.filter(storyid=request_id).order_by('-createtime')[0]
        ret_dict['lfcontent'] = last_fragment.content
    else:
        ret_dict['lock'] = True
    return JsonResponse(data=ret_dict)


def release_lock(request):
    request_id = request.GET.get('story_id')
    story = Story.objects.get(id=request_id)
    ret_dict = {
        'message': "now story" + request_id + " is unlocked"
    }
    
    time.sleep(submit_countdown)
    story.lock = False
    story.save()
        
    return JsonResponse(data=ret_dict)

