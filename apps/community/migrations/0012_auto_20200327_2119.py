# Generated by Django 2.2.3 on 2020-03-27 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0011_auto_20200327_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='desc',
            field=models.TextField(blank=True, verbose_name='描述'),
        ),
    ]
