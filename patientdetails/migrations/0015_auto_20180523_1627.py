# Generated by Django 2.0.3 on 2018-05-23 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patientdetails', '0014_auto_20180523_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testresults',
            name='date',
            field=models.CharField(max_length=30),
        ),
    ]
