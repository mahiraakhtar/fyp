# Generated by Django 2.0.3 on 2018-05-23 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patientdetails', '0007_auto_20180523_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='testresults',
            name='catcode',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patient',
            name='mrno',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='predictedmodel',
            name='discode',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='testresults',
            name='recmon',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='testresults',
            name='recno',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='testresults',
            name='regno',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='testresults',
            name='testcode',
            field=models.CharField(max_length=20),
        ),
    ]