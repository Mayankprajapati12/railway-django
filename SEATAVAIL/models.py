from django.db import models

# Create your models here.
class SeatAvailDB(models.Model):
    ticket_date=models.DateField()
    train_number=models.IntegerField()
    train_name=models.CharField(max_length=50)
    total_seats=models.IntegerField()
    booked_Seats=models.IntegerField()
    remaining_Seats=models.IntegerField() 