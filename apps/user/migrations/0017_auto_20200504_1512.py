# Generated by Django 2.2.3 on 2020-05-04 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_auto_20200428_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='Avatar/default.png', max_length=200, upload_to='Avatar/%Y/%m/%d/', verbose_name='头像'),
        ),
    ]