# Generated by Django 2.2.3 on 2020-04-20 09:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0030_comment_comment_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_num',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='评论数'),
        ),
    ]
