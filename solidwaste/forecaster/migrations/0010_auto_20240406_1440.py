# Generated by Django 3.2.25 on 2024-04-06 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forecaster', '0009_product_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='waste',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='waste',
            name='longitude',
        ),
    ]