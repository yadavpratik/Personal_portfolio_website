# Generated by Django 3.2.5 on 2021-12-01 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0006_auto_20211201_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intro',
            name='skill_intro',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]