# Generated by Django 2.2.3 on 2020-04-28 09:45

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poetry', '0027_auto_20200428_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poet',
            name='achievement',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='成就'),
        ),
        migrations.AlterField(
            model_name='poet',
            name='introduce',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='简介'),
        ),
        migrations.AlterField(
            model_name='poet',
            name='lifetime',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='生平'),
        ),
    ]