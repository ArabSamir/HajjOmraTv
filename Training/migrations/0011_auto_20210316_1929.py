# Generated by Django 3.1.7 on 2021-03-16 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Training', '0010_auto_20210314_0848'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='description',
        ),
        migrations.RemoveField(
            model_name='training',
            name='description',
        ),
    ]