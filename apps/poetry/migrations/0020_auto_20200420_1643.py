# Generated by Django 2.2.3 on 2020-04-20 16:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poetry', '0019_auto_20200420_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poem',
            name='title',
            field=models.CharField(db_index=True, max_length=50, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='poet',
            name='click_num',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='浏览量'),
        ),
        migrations.AlterField(
            model_name='poet',
            name='name',
            field=models.CharField(db_index=True, max_length=20, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='poet',
            name='other_name',
            field=models.CharField(blank=True, db_index=True, max_length=50, null=True, verbose_name='别称'),
        ),
    ]
