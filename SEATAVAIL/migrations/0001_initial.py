# Generated by Django 5.1.1 on 2024-12-02 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SeatAvailDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_date', models.DateField()),
                ('train_number', models.IntegerField()),
                ('train_name', models.CharField(max_length=50)),
                ('total_seats', models.IntegerField()),
                ('booked_Seats', models.IntegerField()),
                ('remaining_Seats', models.IntegerField()),
            ],
        ),
    ]