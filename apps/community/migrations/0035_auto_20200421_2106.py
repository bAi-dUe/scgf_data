# Generated by Django 2.2.3 on 2020-04-21 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0034_auto_20200421_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=30, verbose_name='标题'),
        ),
    ]