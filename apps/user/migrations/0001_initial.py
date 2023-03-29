# Generated by Django 2.2.3 on 2020-03-22 14:55

import django.core.validators
from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='邮箱')),
                ('is_staff', models.BooleanField(default=False, verbose_name='职工')),
                ('is_active', models.BooleanField(default=True, verbose_name='账户状态')),
                ('phone', models.CharField(blank=True, max_length=11, null=True, validators=[django.core.validators.MinLengthValidator(11)], verbose_name='手机')),
                ('nickname', models.CharField(max_length=20, verbose_name='昵称')),
                ('gender', models.CharField(choices=[('male', '男'), ('female', '女')], default='male', max_length=6, verbose_name='性别')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='生日')),
                ('image', models.ImageField(default='Avatar/default.png', upload_to='Avatar/%Y/%m/%d/', verbose_name='头像')),
                ('signature', models.CharField(blank=True, max_length=40, null=True, verbose_name='个性签名')),
                ('address', models.CharField(blank=True, max_length=30, null=True, verbose_name='地址')),
                ('fans', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='粉丝数')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='加入时间')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
            },
            managers=[
                ('objects', user.models.UserManager()),
            ],
        ),
    ]