from .models import *
from rest_framework import serializers

class SeatAvailSerializer(serializers.ModelSerializer):
    model=SeatAvailDB
    fields='__all__'