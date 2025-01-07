from .models import *
from rest_framework import serializers
from django.http import HttpResponse

class SeatAvailSerializer(serializers.ModelSerializer):
    class Meta:
        model=SeatAvailDB
        fields='__all__'

    def create(self, validated_data):
        sa=SeatAvailDB.objects.create(**validated_data)
        return sa 