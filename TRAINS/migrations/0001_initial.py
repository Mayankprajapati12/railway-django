# Generated by Django 5.1.1 on 2024-12-06 07:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TrainData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trainNumber', models.IntegerField(unique=True)),
                ('trainName', models.CharField(max_length=30)),
                ('stationFrom', models.CharField(max_length=30)),
                ('stationTo', models.CharField(max_length=30)),
                ('total_number_of_coaches', models.IntegerField()),
                ('total_seats_train', models.IntegerField()),
                ('runningDays', models.JSONField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='TrainCoaches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coach_class', models.CharField(max_length=50)),
                ('coach_class_code', models.CharField(max_length=15)),
                ('seats_per_coach', models.IntegerField()),
                ('number_of_coaches', models.IntegerField()),
                ('total_seats', models.IntegerField(blank=True, null=True)),
                ('price_per_km', models.DecimalField(decimal_places=18, max_digits=20)),
                ('train_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coaches', to='TRAINS.traindata', to_field='trainNumber')),
            ],
        ),
        migrations.CreateModel(
            name='CoachQuota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('general_seats', models.IntegerField()),
                ('tatkal_seats', models.IntegerField(blank=True, null=True)),
                ('ladies_seats', models.IntegerField(blank=True, null=True)),
                ('senior_citizen_lowerberth_seats', models.IntegerField(blank=True, null=True)),
                ('coach_class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coach_seat_detail', to='TRAINS.traincoaches')),
                ('train_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='forquota', to='TRAINS.traindata', to_field='trainNumber')),
            ],
        ),
        migrations.CreateModel(
            name='TrainStations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stationCode', models.CharField(max_length=20)),
                ('stationName', models.CharField(max_length=20)),
                ('arrivalTime', models.CharField(max_length=20)),
                ('departureTime', models.CharField(max_length=20)),
                ('haltTime', models.CharField(max_length=20)),
                ('distance', models.CharField(max_length=20)),
                ('dayCount', models.IntegerField()),
                ('train_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stations', to='TRAINS.traindata', to_field='trainNumber')),
            ],
        ),
    ]