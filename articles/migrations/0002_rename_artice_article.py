# Generated by Django 4.0.5 on 2022-06-11 13:08

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Artice',
            new_name='Article',
        ),
    ]
