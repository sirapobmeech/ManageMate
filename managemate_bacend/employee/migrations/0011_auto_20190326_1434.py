# Generated by Django 2.1.5 on 2019-03-26 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0010_auto_20190326_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar',
            name='time',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
