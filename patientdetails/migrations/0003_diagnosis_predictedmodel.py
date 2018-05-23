# Generated by Django 2.0.5 on 2018-05-22 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patientdetails', '0002_auto_20180520_0103'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discode', models.IntegerField()),
                ('disease', models.CharField(max_length=500)),
                ('parentcode', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='PredictedModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discode', models.IntegerField()),
                ('disease', models.CharField(max_length=500)),
                ('predicted_disease', models.CharField(max_length=500)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patientdetails.Patient')),
            ],
        ),
    ]
