# Generated by Django 5.1.4 on 2024-12-21 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studys_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Subject',
            new_name='CourseUnit',
        ),
    ]
