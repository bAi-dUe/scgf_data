# Generated by Django 2.2.3 on 2020-05-04 15:12

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0003_banner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=30, verbose_name='反馈主题')),
                ('desc', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='问题描述')),
                ('image', models.ImageField(blank=True, max_length=200, upload_to='feedback/%Y/%m', verbose_name='相关图片')),
                ('contact', models.CharField(blank=True, max_length=50, verbose_name='联系方式')),
            ],
            options={
                'verbose_name_plural': '意见反馈',
                'verbose_name': '意见反馈',
            },
        ),
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(max_length=200, upload_to='banner/%Y/%m', verbose_name='轮播图'),
        ),
    ]
