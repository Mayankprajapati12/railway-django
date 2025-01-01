from django.db import models
from TRAINS.models import TrainData
# Create your models here.
class SeatAvailDB(models.Model):
   train_no=models.ForeignKey(TrainData,to_field="trainNumber",on_delete=models.CASCADE,related_name="seatavail")
   seat_no=models.IntegerField()
   coach=models.CharField(max_length=50)
   seat_type=models.CharField(max_length=5)
   quota=models.CharField(max_length=50)
   jan2=models.JSONField()
   jan3=models.JSONField()