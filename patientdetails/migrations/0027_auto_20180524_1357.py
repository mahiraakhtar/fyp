# Generated by Django 2.0.2 on 2018-05-24 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patientdetails', '0026_auto_20180524_0115'),
    ]

    operations = [
        migrations.CreateModel(
            name='rules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='rules_param',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parameter', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discode', models.CharField(max_length=10)),
                ('disease', models.CharField(max_length=500)),
                ('patient', models.ForeignKey(db_column='mrno', on_delete=django.db.models.deletion.CASCADE, to='patientdetails.Patient', to_field='mrno')),
            ],
        ),
        migrations.AlterField(
            model_name='diagnosis',
            name='discode',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AddField(
            model_name='rules_param',
            name='Diagnosis',
            field=models.ForeignKey(db_column='discode', on_delete=django.db.models.deletion.CASCADE, to='patientdetails.Diagnosis', to_field='discode'),
        ),
        migrations.AddField(
            model_name='rules_param',
            name='test',
            field=models.ForeignKey(db_column='testcode', on_delete=django.db.models.deletion.CASCADE, to='patientdetails.tests', to_field='testcode'),
        ),
    ]
