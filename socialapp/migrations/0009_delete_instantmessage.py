# Generated by Django 4.0 on 2022-06-27 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0008_alter_instantmessage_sender'),
    ]

    operations = [
        migrations.DeleteModel(
            name='instantmessage',
        ),
    ]
