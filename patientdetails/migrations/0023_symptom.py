# Generated by Django 2.0.3 on 2018-05-23 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patientdetails', '0022_delete_infer'),
    ]

    operations = [
        migrations.CreateModel(
            name='symptom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=500)),
                ('common_name', models.CharField(max_length=500)),
            ],
        ),
    ]