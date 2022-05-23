# Generated by Django 4.0.4 on 2022-05-23 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_soldier_email_alter_soldier_phone_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='soldier',
            name='unit',
        ),
        migrations.AlterField(
            model_name='soldier',
            name='rank',
            field=models.CharField(choices=[(1, 'Cadet'), (3, 'Corporal'), (4, 'Sergeant'), (5, 'Lieutenant'), (6, 'Captain'), (7, 'Major'), (8, 'Colonel'), (9, 'Brigadier'), (10, 'General'), (11, 'Field Marshal')], max_length=50),
        ),
    ]