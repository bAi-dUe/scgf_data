# Generated by Django 2.2.3 on 2020-03-27 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0012_auto_20200327_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='image',
            field=models.ImageField(blank=True, upload_to='Topic/%Y/%m/%d/', verbose_name='图片'),
        ),
    ]