# Generated by Django 2.2.3 on 2020-04-11 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='push',
            field=models.BooleanField(default=True, verbose_name='是否推送'),
        ),
    ]
