# Generated by Django 3.0.5 on 2020-08-21 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_auto_20200821_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='date',
            field=models.CharField(max_length=70, null=True),
        ),
    ]