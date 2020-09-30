# Generated by Django 3.0.8 on 2020-07-19 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0004_auto_20200719_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientallergy',
            name='allergy_till_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patientmedication',
            name='medicationcode',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
