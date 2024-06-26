# Generated by Django 4.2.7 on 2023-11-23 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('photo', models.FileField(upload_to='')),
                ('place', models.CharField(max_length=100)),
                ('post', models.CharField(max_length=50)),
                ('pin', models.IntegerField(max_length=20)),
                ('phone', models.BigIntegerField(max_length=15)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.CharField(max_length=50)),
                ('amount', models.FloatField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.FileField(upload_to='')),
                ('quantity', models.IntegerField(max_length=50)),
                ('price', models.FloatField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('status', models.CharField(max_length=50)),
                ('latitude', models.CharField(max_length=50)),
                ('longitude', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.CharField(max_length=50)),
                ('wtype', models.CharField(max_length=50)),
                ('AGENT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forecaster.agent')),
                ('REQUEST', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forecaster.request')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=50)),
                ('age', models.IntegerField(max_length=50)),
                ('phoneno', models.BigIntegerField(max_length=15)),
                ('LOGIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forecaster.login')),
            ],
        ),
        migrations.AddField(
            model_name='request',
            name='USER',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forecaster.user'),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('amount', models.FloatField(max_length=10)),
                ('ORDER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forecaster.order')),
            ],
        ),
        migrations.CreateModel(
            name='Orderdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.CharField(max_length=50)),
                ('price', models.FloatField(max_length=10)),
                ('quantity', models.IntegerField(max_length=50)),
                ('ORDER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forecaster.order')),
                ('PRODUCT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forecaster.product')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='USER',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forecaster.user'),
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('user', models.CharField(max_length=50)),
                ('feedback', models.CharField(max_length=100)),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forecaster.user')),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Complaint', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('reply', models.CharField(max_length=100)),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forecaster.user')),
            ],
        ),
        migrations.AddField(
            model_name='agent',
            name='LOGIN',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forecaster.login'),
        ),
    ]
