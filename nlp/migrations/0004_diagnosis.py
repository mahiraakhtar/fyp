# Generated by Django 2.0.3 on 2018-05-23 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nlp', '0003_auto_20180503_0106'),
    ]

    operations = [
        migrations.CreateModel(
            name='diagnosis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Diagnosis', models.CharField(max_length=200)),
                ('Code', models.CharField(max_length=70)),
            ],
        ),
    ]
