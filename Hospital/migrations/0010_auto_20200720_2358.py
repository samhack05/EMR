# Generated by Django 3.0.8 on 2020-07-20 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0009_auto_20200720_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospitalcircle',
            name='otp',
            field=models.CharField(default=482133, max_length=20),
        ),
    ]
