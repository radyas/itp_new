# Generated by Django 3.1.1 on 2020-09-20 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='documents',
            name='docCode',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
