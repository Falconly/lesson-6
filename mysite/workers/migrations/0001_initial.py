# Generated by Django 4.2 on 2023-05-02 15:19

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=255, verbose_name='ФИО')),
                ('position', models.CharField(max_length=255, verbose_name='Должность')),
                ('telephone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=255, verbose_name='Email')),
                ('adress', models.CharField(blank=True, max_length=255, verbose_name='Адрес')),
                ('photo', models.ImageField(blank=True, upload_to='photos/', verbose_name='Фото сотрудника')),
            ],
            options={
                'verbose_name': 'Сотрудники',
                'verbose_name_plural': 'Сотрудники',
                'ordering': ('id',),
            },
        ),
    ]
