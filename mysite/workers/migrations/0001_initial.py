# Generated by Django 4.2 on 2023-05-01 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('telephone', models.IntegerField()),
                ('email', models.EmailField(max_length=255)),
                ('adress', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='photos/')),
            ],
        ),
    ]
