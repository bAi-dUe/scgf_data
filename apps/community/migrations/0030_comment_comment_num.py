# Generated by Django 2.2.3 on 2020-04-20 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0029_auto_20200416_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_num',
            field=models.IntegerField(default=0),
        ),
    ]
