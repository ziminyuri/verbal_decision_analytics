# Generated by Django 3.1.3 on 2020-11-19 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_option_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='model',
            name='number',
        ),
    ]
