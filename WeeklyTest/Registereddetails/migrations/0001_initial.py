# Generated by Django 4.1.3 on 2023-01-24 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Batch_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='userdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=20)),
                ('Last_name', models.CharField(max_length=20)),
                ('Gender', models.CharField(max_length=10)),
                ('Email', models.EmailField(max_length=254)),
                ('Phone', models.IntegerField()),
                ('Status', models.CharField(default='pending', max_length=20)),
                ('Batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registereddetails.batch')),
                ('Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registereddetails.course')),
            ],
        ),
        migrations.AddField(
            model_name='batch',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registereddetails.course'),
        ),
    ]