# Generated by Django 4.2.7 on 2023-11-25 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forecaster', '0002_wrequest_viewpickupstatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(max_length=50)),
                ('amount', models.FloatField(max_length=10)),
                ('PRODUCT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forecaster.user')),
            ],
        ),
    ]
