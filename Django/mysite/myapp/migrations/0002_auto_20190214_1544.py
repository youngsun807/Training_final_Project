# Generated by Django 2.1.7 on 2019-02-14 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emotion',
            name='datetime',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='word',
            name='datetime',
            field=models.DateField(null=True),
        ),
    ]
