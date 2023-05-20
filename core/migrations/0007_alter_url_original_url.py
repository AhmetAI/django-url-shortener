# Generated by Django 4.1.7 on 2023-05-20 14:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_url_original_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='original_url',
            field=models.URLField(validators=[django.core.validators.URLValidator()]),
        ),
    ]
