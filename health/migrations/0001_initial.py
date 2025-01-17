# Generated by Django 5.0.4 on 2024-04-27 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bdoctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=50)),
                ('shortaddress', models.CharField(max_length=500)),
                ('address', models.TextField()),
                ('phone_no', models.CharField(max_length=50)),
                ('opening_Hours', models.CharField(max_length=50)),
                ('rating', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ddoctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=50)),
                ('shortaddress', models.CharField(max_length=500)),
                ('address', models.TextField()),
                ('phone_no', models.CharField(max_length=50)),
                ('opening_Hours', models.CharField(max_length=50)),
                ('rating', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='hdoctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=50)),
                ('shortaddress', models.CharField(max_length=500)),
                ('address', models.TextField()),
                ('phone_no', models.CharField(max_length=50)),
                ('opening_Hours', models.CharField(max_length=50)),
                ('rating', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='kdoctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=50)),
                ('shortaddress', models.CharField(max_length=500)),
                ('address', models.TextField()),
                ('phone_no', models.CharField(max_length=50)),
                ('opening_Hours', models.CharField(max_length=50)),
                ('rating', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ldoctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=50)),
                ('shortaddress', models.CharField(max_length=500)),
                ('address', models.TextField()),
                ('phone_no', models.CharField(max_length=50)),
                ('opening_Hours', models.CharField(max_length=50)),
                ('rating', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='mdoctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=50)),
                ('shortaddress', models.CharField(max_length=500)),
                ('address', models.TextField()),
                ('phone_no', models.CharField(max_length=50)),
                ('opening_Hours', models.CharField(max_length=50)),
                ('rating', models.CharField(max_length=50)),
            ],
        ),
    ]
