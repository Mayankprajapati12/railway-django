# Generated by Django 5.1.1 on 2024-12-02 08:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PassengerDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Passenger_Name', models.CharField(max_length=50)),
                ('Passenger_Age', models.IntegerField()),
                ('Passenger_Gender', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='TicketDB',
            fields=[
                ('PNR_Number', models.AutoField(primary_key=True, serialize=False)),
                ('Journey_From', models.CharField(max_length=50)),
                ('Journey_To', models.CharField(max_length=50)),
                ('Boarding_Date', models.DateField(blank=True, null=True)),
                ('Boarding_Time', models.CharField(max_length=10)),
                ('Boarding_Station', models.CharField(max_length=50)),
                ('Destination_Arrival_Date', models.DateField(blank=True, null=True)),
                ('Destination_Arrival_Time', models.CharField(max_length=10)),
                ('Journey_Distance', models.IntegerField(blank=True, null=True)),
                ('Train_Number', models.IntegerField(blank=True, null=True)),
                ('Train_Name', models.CharField(max_length=50)),
                ('Seat_Quota', models.CharField(max_length=10)),
                ('Coach_Class', models.CharField(max_length=20)),
                ('Booking_Date', models.DateField(blank=True, null=True)),
                ('Number_Of_Passengers', models.IntegerField(blank=True, null=True)),
                ('Ticket_Price', models.IntegerField(blank=True, null=True)),
                ('Ticket_Status', models.CharField(max_length=10)),
                ('Journey_Status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Mobile_Number', models.IntegerField(unique=True)),
                ('Password', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PassengerSeatDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Booking_Status', models.CharField(max_length=50)),
                ('Current_Status', models.CharField(max_length=50)),
                ('Berth_Coach', models.CharField(blank=True, max_length=50, null=True)),
                ('Berth_Number', models.IntegerField(blank=True, null=True)),
                ('Berth_Type', models.CharField(blank=True, max_length=5, null=True)),
                ('passenger_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='passenger_seat_details', to='USER.passengerdb')),
            ],
        ),
        migrations.AddField(
            model_name='passengerdb',
            name='ticket_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='passenger', to='USER.ticketdb'),
        ),
        migrations.AddField(
            model_name='ticketdb',
            name='User_Mobile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userticket', to='USER.userdb', to_field='Mobile_Number'),
        ),
    ]