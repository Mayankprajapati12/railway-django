# Generated by Django 5.1.6 on 2025-02-19 09:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('TRAINS', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeatAvailDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Seat_no', models.IntegerField()),
                ('Coach_Class', models.CharField(max_length=20)),
                ('Coach', models.CharField(max_length=50)),
                ('Seat_Type', models.CharField(max_length=5)),
                ('Quota', models.CharField(max_length=50)),
                ('Feb16', models.JSONField(null=True)),
                ('Feb17', models.JSONField(null=True)),
                ('Feb18', models.JSONField(null=True)),
                ('Feb19', models.JSONField(null=True)),
                ('Feb20', models.JSONField(null=True)),
                ('Feb21', models.JSONField(null=True)),
                ('Feb22', models.JSONField(null=True)),
                ('Feb23', models.JSONField(null=True)),
                ('Train_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seatavail', to='TRAINS.traindata', to_field='trainNumber')),
            ],
        ),
    ]
