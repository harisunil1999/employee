# Generated by Django 4.2 on 2023-07-05 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('employee_id', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('possition', models.CharField(max_length=200)),
                ('employee_status', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=150)),
            ],
        ),
    ]
