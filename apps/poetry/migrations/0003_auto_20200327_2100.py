# Generated by Django 2.2.3 on 2020-03-27 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poetry', '0002_auto_20200327_2047'),
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
            field=models.TextField(blank=True, null=True, verbose_name='注解'),
        ),
        migrations.AlterField(
            model_name='poem',
            name='appreciation',
            field=models.TextField(blank=True, null=True, verbose_name='鉴赏'),
        ),
        migrations.AlterField(
            model_name='poem',
            name='background',
            field=models.TextField(blank=True, null=True, verbose_name='背景'),
        ),
        migrations.AlterField(
            model_name='poem',
            name='tags',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='标签'),
        ),
        migrations.AlterField(
            model_name='poem',
            name='translation',
            field=models.TextField(blank=True, null=True, verbose_name='译文'),
        ),
        migrations.AlterField(
            model_name='poet',
            name='achievement',
            field=models.TextField(blank=True, null=True, verbose_name='成就'),
        ),
        migrations.AlterField(
            model_name='poet',
            name='introduce',
            field=models.TextField(blank=True, null=True, verbose_name='简介'),
        ),
        migrations.AlterField(
            model_name='poet',
            name='lifetime',
            field=models.TextField(blank=True, null=True, verbose_name='生平'),
        ),
    ]
