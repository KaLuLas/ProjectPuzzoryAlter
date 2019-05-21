from django.shortcuts import render
from PuzzModel.models import Story, Fragment, UserExtension
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator

index_dict = {
        'display': 'homepage',
        'story_list': '',
        'user_list': '',
        'story_full_list': ''
    }


def homepage(request):
    index_dict['display'] = 'homepage'
    index_dict['story_list'] = Story.objects.order_by('-likescount')[:5]
    index_dict['user_list'] = UserExtension.objects.order_by('-experience')[:5]
    index_dict['story_full_list'] = Story.objects.order_by('-createtime')
    # for Pagination
    story_full_list = Story.objects.order_by('-createtime')
    paginator = Paginator(story_full_list, 10)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    index_dict['paginator'] = paginator
    index_dict['page_obj'] = page_obj
    index_dict['is_paginated'] = True
    return render(request, 'index.html', index_dict)


def storypage(request, story_id):
    story_dict = {
        'story': Story.objects.get(id=story_id),
        'frag_list': Fragment.objects.filter(storyid=story_id).order_by('createtime')
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
        story_record.save()

    story_dict = {
        'story': Story.objects.get(id=story_id),
        'frag_list': Fragment.objects.filter(storyid=story_id).order_by('createtime')
     }
    return render(request, 'story.html', story_dict)


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
