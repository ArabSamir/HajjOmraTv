# Generated by Django 3.1.7 on 2021-03-16 18:29

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0009_category_nb_posts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='المحتوى'),
        ),
    ]
