# Generated by Django 2.2.3 on 2020-03-27 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20200327_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default='Avatar/default.png', upload_to='Avatar/%Y/%m/%d/', verbose_name='头像'),
        ),
    ]