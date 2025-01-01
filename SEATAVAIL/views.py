from .models import *
from TRAINS.models import *
from TRAINS.serializers import *
from USER.models import *
from USER.serializers import *
from .serializers import *
from rest_framework import viewsets
from django.db.models import Q
# Create your views here.
class AvailView(viewsets.ModelViewSet):
    queryset=SeatAvailDB.objects.all()
    serializer_class=SeatAvailSerializer

def getseat(request):
    t=SeatAvailDB.objects.filter(jan2__contains=[7])
    print("t::",t)
    
# @api_view(['GET','POST'])
# def Seat(request,tkt):
#     # print(tkt['userticket'])
#     ticket_details=SeatAvailDB.objects.filter(ticket_date=tkt['Boarding_Date'],train_number=tkt['Train_Number'])
#     train_data=TrainData.objects.get(trainNumber=tkt['Train_Number'])
#     # print("ticket_details::",ticket_details)
#     if ticket_details:
#         booked_tickets=SeatAvailDB.objects.get(ticket_date=tkt['Boarding_Date'],train_number=tkt['Train_Number'])
#         bs=booked_tickets.booked_Seats
#         # print("bs::",bs)
#         booked_tickets.booked_Seats=bs+tkt['Number_Of_Passengers']
#         print("new pas num::",tkt['Number_Of_Passengers'])
#         booked_tickets.total_seats=train_data.total_seats_train
#         booked_tickets.remaining_Seats=booked_tickets.total_seats- booked_tickets.booked_Seats
#         booked_tickets.save()
#         return "seat created!"
#     else:
#         temp={'ticket_date':tkt['Boarding_Date'],
#               'train_number':tkt['Train_Number'],
#               'total_seats':train_data.total_seats_train,
#               'booked_Seats':tkt['Number_Of_Passengers'],
#               'remaining_Seats':train_data.total_seats_train-tkt['Number_Of_Passengers'],
#             }
#         booked_tickets=SeatAvailDB.objects.create(**temp)
#         return "seat created!"