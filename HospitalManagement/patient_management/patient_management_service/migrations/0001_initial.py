# Generated by Django 4.1.13 on 2024-05-30 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'accounts',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('no_house', models.CharField(max_length=255)),
                ('street', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'address',
            },
        ),
        migrations.CreateModel(
            name='FullName',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'full_names',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField()),
                ('is_active', models.IntegerField(default=1)),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='patient_management_service.account')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_management_service.address')),
                ('full_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_management_service.fullname')),
            ],
            options={
                'db_table': 'patients',
            },
        ),
        migrations.CreateModel(
            name='HealthRecord',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('visit_date', models.DateTimeField()),
                ('diagnosis', models.TextField()),
                ('treatment', models.TextField()),
                ('description', models.TextField()),
                ('doctor_id', models.IntegerField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_management_service.patient')),
            ],
            options={
                'db_table': 'health_records',
            },
        ),
    ]