# Generated by Django 4.1.3 on 2023-02-03 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registereddetails', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='Username',
            field=models.CharField(default='null', max_length=20, unique=True),
        ),
    ]
