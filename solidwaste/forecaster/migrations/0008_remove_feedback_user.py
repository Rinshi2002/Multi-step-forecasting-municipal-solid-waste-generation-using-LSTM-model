# Generated by Django 4.2.7 on 2024-02-08 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forecaster', '0007_remove_orderdetails_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='user',
        ),
    ]
