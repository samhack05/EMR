# Generated by Django 3.0.8 on 2020-07-20 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0008_auto_20200720_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientallergy',
            name='dateadd',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='patientmedication',
            name='dateadd',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='patientprescription',
            name='dateadd',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='patientproblem',
            name='dateadd',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='patientsymtoms',
            name='dateadd',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
