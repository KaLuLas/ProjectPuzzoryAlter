# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),) 


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Fragment(models.Model):
    storyid = models.IntegerField()
    nickname = models.CharField(max_length=20)
    email = models.CharField(max_length=150)
    content = models.CharField(max_length=500)
    createtime = models.DateTimeField(default=timezone.now)
    likescount = models.IntegerField(default=0)  
    commentscount = models.IntegerField(default=0)   
    branchid = models.IntegerField(default=0)
    branchleft = models.IntegerField(blank=True, null=True) 
    branchright = models.IntegerField(blank=True, null=True) 


class Story(models.Model):
    ffid = models.IntegerField()
    ffcontent = models.CharField(max_length=500)
    nickname = models.CharField(max_length=20)
    editor = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    title = models.CharField(max_length=50)
    createtime = models.DateTimeField(default=timezone.now)
    updatetime = models.DateTimeField(default=timezone.now)
    remains = models.IntegerField(default=0)
    branch = models.BooleanField(default=False)
    finished = models.BooleanField(default=False)
    lock = models.BooleanField(default=False)
    modified = models.BooleanField(default=True)
    likescount = models.IntegerField(default=0)  
    commentscount = models.IntegerField(default=0)
    fragscount = models.IntegerField(default=1)
    fragscountlimit = models.IntegerField(default=-1)
    fragwordslimit = models.IntegerField(default=-1) 


class UserExtension(User):
    nickname = models.CharField(max_length=20)  
    level = models.IntegerField(default=1)
    experience = models.IntegerField(default=0)
    avator = models.ImageField(blank=True)


class Comment(models.Model):
    nickname = models.CharField(max_length=20)
    email = models.CharField(max_length=150)
    sof = models.BooleanField()
    storyid = models.IntegerField(blank=True, null=True)
    fragid = models.IntegerField(blank=True, null=True)
    content = models.CharField(max_length=150)
    createtime = models.DateTimeField(default=timezone.now)
    likescount = models.IntegerField(default=0) 


class Announcement(models.Model):
    optype = models.CharField(max_length=20) #addfrag/storylike/fraglike//storycomment/fragcomment/cocomment
    targetid = models.IntegerField()
    fromuser = models.CharField(max_length=150)
    fromnickname = models.CharField(max_length=20)
    touser = models.CharField(max_length=150)
    tonickname = models.CharField(max_length=20)
    createtime = models.DateTimeField(default=timezone.now)
    content = models.CharField(max_length=150, blank=True, null=True)
    read = models.BooleanField(default=False)


