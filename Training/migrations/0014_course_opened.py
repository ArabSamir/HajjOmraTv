# Generated by Django 3.1.7 on 2021-03-25 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Training', '0013_auto_20210317_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='opened',
            field=models.BooleanField(default=False, verbose_name='حالة الدرس'),
        ),
    ]
