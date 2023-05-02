# Generated by Django 4.2 on 2023-05-01 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0003_alter_worker_telephone'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='worker',
            options={'ordering': ('id',), 'verbose_name': 'Сотрудники', 'verbose_name_plural': 'Сотрудники'},
        ),
        migrations.AlterField(
            model_name='worker',
            name='telephone',
            field=models.CharField(max_length=12, verbose_name='Телефон'),
        ),
    ]
