# Generated by Django 2.2.5 on 2019-09-03 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shujog', '0002_auto_20190903_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
