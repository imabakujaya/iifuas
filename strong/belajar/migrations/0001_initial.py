# Generated by Django 4.1.2 on 2022-12-27 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Managemen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Organisasi', models.CharField(max_length=40)),
                ('Pemimpin', models.CharField(max_length=75)),
            ],
        ),
    ]