# Generated by Django 3.1.7 on 2021-03-04 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0009_video_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='about_us_image',
            field=models.ImageField(default='../static/img/photo1.jpg', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='content',
            name='favicon',
            field=models.ImageField(default='../static/img/photo1.jpg', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='content',
            name='header_image',
            field=models.ImageField(default='../static/img/photo1.jpg', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='content',
            name='logo',
            field=models.ImageField(default='../static/img/photo1.jpg', upload_to='images/'),
        ),
    ]