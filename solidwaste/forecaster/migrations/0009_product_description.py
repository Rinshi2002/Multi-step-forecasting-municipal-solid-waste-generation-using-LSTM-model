# Generated by Django 3.2.25 on 2024-04-06 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forecaster', '0008_remove_feedback_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]