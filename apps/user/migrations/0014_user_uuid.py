# Generated by Django 2.2.3 on 2020-04-21 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_auto_20200420_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='uuid',
            field=models.CharField(default='1', max_length=32),
        ),
    ]
