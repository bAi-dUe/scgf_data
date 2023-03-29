# Generated by Django 2.2.3 on 2020-04-20 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_user_is_follow'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.IntegerField(default=0, verbose_name='城市代码'),
        ),
        migrations.AddField(
            model_name='user',
            name='province',
            field=models.IntegerField(default=0, verbose_name='省份代码'),
        ),
    ]
