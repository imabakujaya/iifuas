# Generated by Django 4.1.2 on 2022-12-25 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pengurus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bph', models.CharField(max_length=70)),
                ('devisi', models.CharField(max_length=75)),
                ('co_anggota', models.CharField(max_length=200)),
                ('departemen', models.CharField(max_length=210)),
            ],
        ),
    ]
