# Generated by Django 4.0.4 on 2022-05-23 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_weapon_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weapon',
            name='weapon_id',
            field=models.CharField(blank=True, max_length=50, unique=True),
        ),
    ]
