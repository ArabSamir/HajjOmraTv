# Generated by Django 3.1.7 on 2021-03-08 13:13

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Training', '0006_auto_20210308_1333'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usertraining',
            options={'verbose_name': 'الطلب', 'verbose_name_plural': 'الطلبات'},
        ),
        migrations.AlterField(
            model_name='course',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='المحتوى'),
        ),
        migrations.AlterField(
            model_name='section',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='المحتوى'),
        ),
        migrations.AlterField(
            model_name='training',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='المحتوى'),
        ),
    ]
