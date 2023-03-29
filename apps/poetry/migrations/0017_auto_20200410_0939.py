# Generated by Django 2.2.3 on 2020-04-10 09:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poetry', '0016_auto_20200410_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taggeditem',
            name='tag',
            field=models.CharField(max_length=12, validators=[django.core.validators.MinLengthValidator(1)], verbose_name='标签'),
        ),
    ]