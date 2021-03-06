# Generated by Django 3.1.7 on 2021-03-04 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0007_auto_20210303_2223'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_on'], 'verbose_name': 'التعليق', 'verbose_name_plural': 'التعليقات'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_on'], 'verbose_name': 'مقال', 'verbose_name_plural': 'مقالات'},
        ),
        migrations.AlterField(
            model_name='post',
            name='nb_comments',
            field=models.IntegerField(default=0, verbose_name='عدد التعليقات'),
        ),
    ]
