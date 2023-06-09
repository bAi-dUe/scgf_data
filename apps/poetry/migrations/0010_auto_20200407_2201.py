# Generated by Django 2.2.3 on 2020-04-07 22:01

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poetry', '0009_remove_mingju_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mingju',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='poem',
            name='annotation',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='注解'),
        ),
        migrations.AlterField(
            model_name='poem',
            name='appreciation',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='鉴赏'),
        ),
        migrations.AlterField(
            model_name='poem',
            name='background',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='背景'),
        ),
        migrations.AlterField(
            model_name='poem',
            name='image',
            field=models.ImageField(blank=True, default='Poem/default.png', null=True, upload_to='Poem/%Y/%m/%d/', verbose_name='情景图片'),
        ),
        migrations.AlterField(
            model_name='poem',
            name='tags',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='标签'),
        ),
        migrations.AlterField(
            model_name='poem',
            name='translation',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='译文'),
        ),
        migrations.AlterField(
            model_name='poet',
            name='achievement',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='成就'),
        ),
        migrations.AlterField(
            model_name='poet',
            name='image',
            field=models.ImageField(blank=True, default='Poet/default.png', null=True, upload_to='Poet/%Y/%m/%d/', verbose_name='肖像'),
        ),
        migrations.AlterField(
            model_name='poet',
            name='introduce',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='简介'),
        ),
        migrations.AlterField(
            model_name='poet',
            name='lifetime',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='生平'),
        ),
        migrations.AlterField(
            model_name='poet',
            name='other_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='别称'),
        ),
        migrations.AlterField(
            model_name='poet',
            name='remark',
            field=models.IntegerField(default=-1, null=True, unique=True),
        ),
    ]
