# Generated by Django 4.0.4 on 2022-05-23 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_weaponsubcategory_weaponcategory_fa_object_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='weapon',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
