from django.db import models
from TRAINS.models import TrainData
# Create your models here.
class SeatAvailDB(models.Model):
   train_no=models.ForeignKey(TrainData,to_field="trainNumber",on_delete=models.CASCADE,related_name="seatavail")
   seat_no=models.IntegerField()
   coach_class=models.CharField(max_length=20)
   coach=models.CharField(max_length=50)
   seat_type=models.CharField(max_length=5)
   quota=models.CharField(max_length=50)
   jan3=models.JSONField(null=True)
   jan4=models.JSONField(null=True)
   jan5=models.JSONField(null=True)
   