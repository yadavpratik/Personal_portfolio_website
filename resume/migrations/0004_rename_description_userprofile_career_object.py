# Generated by Django 3.2.5 on 2021-12-01 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_rename_psition_experience_position'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='description',
            new_name='career_object',
        ),
    ]
