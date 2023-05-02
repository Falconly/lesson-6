# Generated by Django 4.2 on 2023-05-02 08:18

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0009_alter_worker_is_monthworker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='telephone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True, verbose_name='Телефон'),
        ),
    ]
