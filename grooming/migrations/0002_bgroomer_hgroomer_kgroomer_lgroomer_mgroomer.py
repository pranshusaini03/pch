# Generated by Django 5.0.4 on 2024-04-27 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grooming', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bgroomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=50)),
                ('shortaddress', models.CharField(max_length=500)),
                ('address', models.TextField()),
                ('phone_no', models.CharField(max_length=50)),
                ('opening_Hours', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='hgroomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=50)),
                ('shortaddress', models.CharField(max_length=500)),
                ('address', models.TextField()),
                ('phone_no', models.CharField(max_length=50)),
                ('opening_Hours', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='kgroomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=50)),
                ('shortaddress', models.CharField(max_length=500)),
                ('address', models.TextField()),
                ('phone_no', models.CharField(max_length=50)),
                ('opening_Hours', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='lgroomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=50)),
                ('shortaddress', models.CharField(max_length=500)),
                ('address', models.TextField()),
                ('phone_no', models.CharField(max_length=50)),
                ('opening_Hours', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='mgroomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=50)),
                ('shortaddress', models.CharField(max_length=500)),
                ('address', models.TextField()),
                ('phone_no', models.CharField(max_length=50)),
                ('opening_Hours', models.CharField(max_length=50)),
            ],
        ),
    ]
