# Generated by Django 4.1.7 on 2023-05-17 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_url_short_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='url',
            old_name='short_url',
            new_name='short_url_slug',
        ),
    ]