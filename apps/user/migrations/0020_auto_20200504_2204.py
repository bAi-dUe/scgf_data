# Generated by Django 2.2.3 on 2020-05-04 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0019_auto_20200504_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='content',
            field=models.CharField(default='故不登高山，不知天之高也；不临深溪，不知地之厚也；', max_length=40, verbose_name='内容'),
        ),
    ]