# Generated by Django 3.1.7 on 2021-03-31 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0015_content_ccp'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='logo_white',
            field=models.ImageField(default='../static/img/photo1.jpg', upload_to='images/', verbose_name='صورة الشعار الأبيض'),
        ),
    ]