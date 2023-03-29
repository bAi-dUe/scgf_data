# Generated by Django 2.2.3 on 2020-04-21 17:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0033_auto_20200421_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='dynamic',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
