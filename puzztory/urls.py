"""puzztory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from . import view, user, testdb

urlpatterns = [
    path('', view.homepage, name="index"),
    path('userlogin', user.Login, name="login"),
    path('userregister', user.register, name="register"),
    path('login', view.login_page, name="login_page"),
    path('register', view.register_page, name="register_page"),
    path('logout', user.Logout, name="logout"),
    path('user/<nickname>', user.userpage, name="user_page"),
    path('upload', view.upload_story_page, name="upload_story_page"),
    path('message', view.system_message, name="system_message"),
    path('uploading', view.upload_story, name="upload_story"),
    path('story/adding/<int:story_id>', view.upload_frag, name="upload_frag"),
    path('story/<int:story_id>', view.storypage, name="story_page"),
    re_path(r'^lock', view.lock, name="lock"),
    re_path(r'^testdb$', testdb.testdb),  # edit
    path('admin/', admin.site.urls),
]
