# Generated by Django 4.1.7 on 2023-05-04 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors_name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('notes', models.TextField()),
                ('doctors', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.doctors_name')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicines', models.CharField(max_length=50)),
                ('causes', models.CharField(max_length=50)),
                ('symptoms', models.CharField(max_length=50)),
                ('file', models.FileField(upload_to='files')),
                ('comments', models.TextField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.patient')),
            ],
        ),
    ]
