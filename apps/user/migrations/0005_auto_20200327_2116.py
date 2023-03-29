# Generated by Django 2.2.3 on 2020-03-27 21:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20200327_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=30, verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=11, validators=[django.core.validators.MinLengthValidator(11)], verbose_name='手机'),
        ),
        migrations.AlterField(
            model_name='user',
            name='signature',
            field=models.CharField(blank=True, max_length=40, verbose_name='个性签名'),
        ),
    ]
