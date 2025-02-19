from django.db import models

class TrainData(models.Model):
    trainNumber=models.IntegerField(unique=True)
    trainName=models.CharField(max_length=30)
    stationFrom=models.CharField(max_length=30)
    stationTo=models.CharField(max_length=30)
    total_number_of_coaches=models.IntegerField()
    total_seats_train=models.IntegerField()
    runningDays=models.JSONField()
    
class TrainStations(models.Model):
    train_no=models.ForeignKey(TrainData,to_field='trainNumber',on_delete=models.CASCADE,related_name="stations")
    stationCode=models.CharField(max_length=20)
    stationName=models.CharField(max_length=20)
    arrivalTime=models.CharField(max_length=20)
    departureTime=models.CharField(max_length=20)
    haltTime=models.CharField(max_length=20)
    distance=models.CharField(max_length=20)
    dayCount=models.IntegerField()
    
class TrainCoaches(models.Model):
    train_no=models.ForeignKey(TrainData,to_field='trainNumber',on_delete=models.CASCADE,related_name="coaches")
    coach_class=models.CharField(max_length=50)
    coach_class_code=models.CharField(max_length=15)
    seats_per_coach=models.IntegerField()
    number_of_coaches=models.IntegerField()
    total_seats=models.IntegerField(null=True,blank=True)
    price_per_km=models.DecimalField(max_digits=20,decimal_places=18)
    
class CoachQuota(models.Model):
    train_no=models.ForeignKey(TrainData,to_field='trainNumber',on_delete=models.CASCADE,related_name='forquota')
    coach_class_id=models.ForeignKey(TrainCoaches,on_delete=models.CASCADE,related_name='coach_seat_detail')
    general_seats=models.IntegerField()
    tatkal_seats=models.IntegerField(null=True,blank=True)
    ladies_seats=models.IntegerField(null=True,blank=True)
    senior_citizen_lowerberth_seats=models.IntegerField(null=True,blank=True)