from .models import *
from rest_framework import serializers

class CoachQuotaSerialzier(serializers.ModelSerializer):
    class Meta:
        model=CoachQuota
        fields=['general_seats','tatkal_seats','ladies_seats','senior_citizen_lowerberth_seats']
        
class TrainCoachSerializer(serializers.ModelSerializer):
    coach_seat_detail=CoachQuotaSerialzier(many=True,required=False)
    class Meta:
        model=TrainCoaches
        fields=['coach_class','coach_class_code','seats_per_coach','number_of_coaches','total_seats','price_per_km','coach_seat_detail']
        
class TrainStationSerializer(serializers.ModelSerializer):
    class Meta:
        model=TrainStations
        fields=['train_no_id','id','stationCode','stationName','departureTime','arrivalTime','haltTime','distance','dayCount']
        
class TrainSerializer(serializers.ModelSerializer):
    stations=TrainStationSerializer(many=True)
    coaches=TrainCoachSerializer(many=True,required=False)
    class Meta:
        model=TrainData
        fields=['trainNumber','trainName','stationFrom','stationTo','total_number_of_coaches','runningDays','stations','coaches']
                
    def create(self,validated_data):
        # print("vd::",validated_data)
        station_details=validated_data.pop("stations")
        coach_Details=validated_data.pop("coaches")
        total_seats=0
        for seats in coach_Details:
            total=seats['seats_per_coach']*seats['number_of_coaches']
            total_seats=total_seats+total
        validated_data['total_seats_train']=total_seats
        train=TrainData.objects.create(**validated_data)
        for s in station_details:
            TrainStations.objects.create(train_no=train,**s)
        for i in coach_Details:
            temp=i
            temp['total_seats']=i['number_of_coaches']*i['seats_per_coach']
            coach_Seat_details=i.pop("coach_seat_detail")
            cd=TrainCoaches.objects.create(train_no=train,**temp)
            for j in coach_Seat_details:
                tem=j
                tem['general_seats']=j['general_seats']*i['number_of_coaches']
                tem['tatkal_seats']=0 if j['tatkal_seats'] is None else int(j['tatkal_seats'])*i['number_of_coaches']
                tem['ladies_seats']=0 if j['ladies_seats'] is None else int(j['ladies_seats'])*i['number_of_coaches']
                tem['senior_citizen_lowerberth_seats']=0 if j['senior_citizen_lowerberth_seats'] is None else int(j['senior_citizen_lowerberth_seats'])*i['number_of_coaches']           
                CoachQuota.objects.create(train_no=train,coach_class_id=cd,**tem)
        return train            