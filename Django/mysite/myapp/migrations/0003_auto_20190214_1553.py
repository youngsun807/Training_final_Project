# Generated by Django 2.1.7 on 2019-02-14 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20190214_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emotion',
            name='datetime',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='word',
            name='datetime',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]