# Generated by Django 3.1.7 on 2021-03-14 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Training', '0009_auto_20210314_0840'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['order'], 'verbose_name': 'الدرس', 'verbose_name_plural': 'الدروس'},
        ),
        migrations.AlterModelOptions(
            name='section',
            options={'ordering': ['order'], 'verbose_name': 'الوحدة', 'verbose_name_plural': 'الوحدات'},
        ),
    ]
