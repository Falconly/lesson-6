# Generated by Django 4.2 on 2023-05-01 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0005_alter_worker_telephone'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='is_monthworker',
            field=models.BooleanField(default=True, verbose_name='Сотрудник месяца'),
        ),
    ]