# Generated by Django 2.1.5 on 2019-04-03 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0019_project'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='Comment',
            new_name='comment',
        ),
    ]