# Generated by Django 2.0.3 on 2018-05-23 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patientdetails', '0011_auto_20180523_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='mrno',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='predictedmodel',
            name='patient',
            field=models.ForeignKey(db_column='name', on_delete=django.db.models.deletion.CASCADE, to='patientdetails.Patient', to_field='mrno'),
        ),
    ]
