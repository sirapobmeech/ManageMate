# Generated by Django 2.1.5 on 2019-03-26 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0015_auto_20190326_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]