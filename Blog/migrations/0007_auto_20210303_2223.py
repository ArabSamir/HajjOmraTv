# Generated by Django 3.1.7 on 2021-03-03 21:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Blog', '0006_auto_20210303_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='nb_comments',
            field=models.IntegerField(default=0, verbose_name='الحالة'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='تعلسق')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='المعلق')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blog.post', verbose_name='المقال')),
            ],
        ),
    ]