# Generated by Django 5.0.4 on 2024-04-28 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_gform_hform'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='gform',
            new_name='groomingform',
        ),
        migrations.RenameModel(
            old_name='hform',
            new_name='healthform',
        ),
    ]
