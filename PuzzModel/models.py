# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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


class Commenttable(models.Model):
    commentid = models.AutoField(db_column='commentID', primary_key=True)  # Field name made lowercase.
    storyid = models.IntegerField(db_column='storyID')  # Field name made lowercase.
    fragmentid = models.IntegerField(db_column='fragmentID')  # Field name made lowercase.
    content = models.TextField()
    username = models.CharField(db_column='userName', max_length=50)  # Field name made lowercase.
    useremail = models.CharField(db_column='userEmail', max_length=50)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime')  # Field name made lowercase.
    likescount = models.IntegerField(db_column='likesCount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'commentTable'


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


class Fragmenttable(models.Model):
    username = models.CharField(db_column='userName', max_length=50)  # Field name made lowercase.
    useremail = models.CharField(db_column='userEmail', max_length=50)  # Field name made lowercase.
    content = models.TextField()
    createtime = models.DateTimeField(db_column='createTime')  # Field name made lowercase.
    commentscount = models.IntegerField(db_column='commentsCount', blank=True, null=True)  # Field name made lowercase.
    likescount = models.IntegerField(db_column='likesCount', blank=True, null=True)  # Field name made lowercase.
    storyid = models.IntegerField(db_column='storyID')  # Field name made lowercase.
    branchid = models.IntegerField(db_column='branchID')  # Field name made lowercase.
    branchleft = models.IntegerField(db_column='branchLeft', blank=True, null=True)  # Field name made lowercase.
    branchright = models.IntegerField(db_column='branchRight', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'fragmentTable'


class Storytable(models.Model):
    username = models.CharField(db_column='userName', max_length=50)  # Field name made lowercase.
    useremail = models.CharField(db_column='userEmail', max_length=50)  # Field name made lowercase.
    title = models.CharField(max_length=50)
    likescount = models.IntegerField(db_column='likesCount', blank=True, null=True)  # Field name made lowercase.
    fragmentcapacity = models.IntegerField(db_column='fragmentCapacity', blank=True, null=True)  # Field name made lowercase.
    fragmentscount = models.IntegerField(db_column='fragmentsCount', blank=True, null=True)  # Field name made lowercase.
    branch = models.CharField(max_length=1, blank=True, null=True)
    wordslimit = models.CharField(db_column='wordsLimit', max_length=1, blank=True, null=True)  # Field name made lowercase.
    finished = models.CharField(max_length=1, blank=True, null=True)
    modified = models.CharField(max_length=1, blank=True, null=True)
    createtime = models.DateTimeField(db_column='createTime')  # Field name made lowercase.
    beginning = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'storyTable'


class Usertable(models.Model):
    useremail = models.CharField(db_column='userEmail', primary_key=True, max_length=50)  # Field name made lowercase.
    username = models.CharField(db_column='userName', max_length=50)  # Field name made lowercase.
    password = models.CharField(max_length=256, blank=True, null=True)
    level = models.IntegerField(blank=True, null=True, default=1)
    experience = models.IntegerField(blank=True, null=True, default=0)

    class Meta:
        # managed = False
        db_table = 'userTable'
