# Generated by Django 2.2.3 on 2020-03-27 20:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0009_auto_20200326_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(5)], verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='desc',
            field=models.TextField(blank=True, verbose_name='描述'),
        ),
    ]
