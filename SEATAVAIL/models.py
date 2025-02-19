from django.db import models
from TRAINS.models import TrainData
# Create your models here.
class SeatAvailDB(models.Model):
   Train_no=models.ForeignKey(TrainData,to_field="trainNumber",on_delete=models.CASCADE,related_name="seatavail")
   Seat_no=models.IntegerField()
   Coach_Class=models.CharField(max_length=20)
   Coach=models.CharField(max_length=50)
   Seat_Type=models.CharField(max_length=5)
   Quota=models.CharField(max_length=50)
   Feb17=models.JSONField(null=True)
   Feb18=models.JSONField(null=True)
   Feb19=models.JSONField(null=True)
   Feb20=models.JSONField(null=True)
   Feb21=models.JSONField(null=True)
   Feb22=models.JSONField(null=True)
   Feb23=models.JSONField(null=True)
   Feb24=models.JSONField(null=True)