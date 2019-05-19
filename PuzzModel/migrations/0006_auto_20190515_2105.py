# Generated by Django 2.2 on 2019-05-15 21:05

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('PuzzModel', '0005_auto_20190513_0041'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserExtension',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('nickname', models.CharField(max_length=20)),
                ('level', models.IntegerField(default=1)),
                ('experience', models.IntegerField(default=0)),
                ('avator', models.ImageField(blank=True, upload_to='')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.DeleteModel(
            name='Usertable',
        ),
    ]