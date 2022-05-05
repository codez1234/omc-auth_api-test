# Generated by Django 4.0.3 on 2022-05-04 08:04

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email')),
                ('phone_number', models.IntegerField(unique=True, verbose_name='Phone_Number')),
                ('password', models.CharField(max_length=50, validators=[users.models.validate_password])),
                ('name', models.CharField(max_length=200)),
                ('is_omc', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]