# Generated by Django 3.1.7 on 2021-03-31 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Training', '0016_training_statut'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='الثمن'),
        ),
        migrations.AlterField(
            model_name='training',
            name='price_dzd',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='الثمن'),
        ),
    ]
