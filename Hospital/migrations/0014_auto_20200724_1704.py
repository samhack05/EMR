# Generated by Django 3.0.8 on 2020-07-24 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0013_auto_20200724_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospitalcircle',
            name='otp',
            field=models.CharField(default=993674, max_length=20),
        ),
        migrations.AlterField(
            model_name='labcircle',
            name='otp',
            field=models.CharField(default=429574, max_length=20),
        ),
    ]
