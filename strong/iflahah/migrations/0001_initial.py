# Generated by Django 4.1.2 on 2022-12-27 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rutinitas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('istighosah', models.CharField(max_length=30)),
                ('kajian', models.CharField(max_length=30)),
            ],
        ),
    ]
