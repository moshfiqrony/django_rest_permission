# Generated by Django 2.2.5 on 2019-09-03 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shujog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='lasrName',
            new_name='lastName',
        ),
    ]
