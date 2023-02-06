# Generated by Django 4.1.3 on 2023-01-27 14:13

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
                ('Batch_id', models.IntegerField(primary_key=True, serialize=False)),
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
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='userdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=20)),
                ('Last_name', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
                ('Phone', models.CharField(max_length=10)),
                ('Status', models.CharField(default='pending', max_length=20)),
                ('Batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registereddetails.batch')),
                ('Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registereddetails.course')),
                ('Gender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Registereddetails.gender')),
            ],
        ),
        migrations.AddField(
            model_name='batch',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registereddetails.course'),
        ),
    ]
