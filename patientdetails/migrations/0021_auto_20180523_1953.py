# Generated by Django 2.0.3 on 2018-05-23 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patientdetails', '0020_infer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infer',
            name='age',
            field=models.IntegerField(),
        ),
    ]
