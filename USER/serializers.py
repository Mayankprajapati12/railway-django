from rest_framework import serializers
from .models import *

class PassengerSeatSerializer(serializers.ModelSerializer):
    class Meta:
        model=PassengerSeatDB
        fields='__all__'
        
class PasssengerSerializer(serializers.ModelSerializer):
    passenger_seat_details=PassengerSeatSerializer()
    class Meta:
        model=PassengerDB
        fields='__all__'
        
class TicketDBSerializer(serializers.ModelSerializer):
    passenger=PasssengerSerializer(many=True)
    class Meta:
        model=TicketDB
        fields='__all__'
        
class UserDBSerializer(serializers.ModelSerializer):
    userticket=TicketDBSerializer(many=True,required=False)
    class Meta:
        model=UserDB
        fields='__all__'