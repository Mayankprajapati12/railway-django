from django.http import JsonResponse,HttpResponse
from rest_framework import viewsets
from .serializers import *
from .models import *

class TrainView(viewsets.ModelViewSet):
    queryset = TrainData.objects.all()
    serializer_class = TrainSerializer
    
# def test(request):
#     s=TrainStations.objects.filter(train_no=12920)
#     f=TrainStations.objects.get(train_no=12920,stationCode='JAT')
#     e=TrainStations.objects.get(train_no=12920,stationCode='SIR')
#     new=[]
#     for i in range(f.id,e.id):
#         q=TrainStations.objects.get(id=i)
#         new.append(q)
#     x=TrainStationSerializer(new,many=True)
#     print("x::",x.data) 