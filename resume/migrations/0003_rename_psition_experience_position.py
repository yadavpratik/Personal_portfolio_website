# Generated by Django 3.2.5 on 2021-11-30 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_auto_20211130_1209'),
    ]

    operations = [
        migrations.RenameField(
            model_name='experience',
            old_name='psition',
            new_name='position',
        ),
    ]