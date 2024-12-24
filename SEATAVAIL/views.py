from django.shortcuts import render
from .models import *
from TRAINS.models import *
from TRAINS.serializers import *
from USER.models import *
from USER.serializers import *
from rest_framework.decorators import api_view
from django.http import HttpResponse
# Create your views here.
# @api_view(['GET','POST'])
# def Seat(request,tkt):
#     # print(tkt['userticket'])
#     ticket_details=SeatAvailDB.objects.filter(ticket_date=tkt['userticket']['Boarding_Date'],train_number=tkt['userticket']['Train_Number'])
#     train_data=TrainData.objects.get(trainNumber=tkt['userticket']['Train_Number'])
#     # print("ticket_details::",ticket_details)
#     if ticket_details:
#         booked_tickets=SeatAvailDB.objects.get(ticket_date=tkt['userticket']['Boarding_Date'],train_number=tkt['userticket']['Train_Number'])
#         bs=booked_tickets.booked_Seats
#         # print("bs::",bs)
#         booked_tickets.booked_Seats=bs+tkt['userticket']['Number_Of_Passengers']
#         print("new pas num::",tkt['userticket']['Number_Of_Passengers'])
#         booked_tickets.total_seats=train_data.total_seats_train
#         booked_tickets.remaining_Seats=booked_tickets.total_seats- booked_tickets.booked_Seats
#         booked_tickets.save()
#         return HttpResponse("seat updated!")
#     else:
#         temp={'ticket_date':tkt['userticket']['Boarding_Date'],
#               'train_number':tkt['userticket']['Train_Number'],
#               'total_seats':train_data.total_seats_train,
#               'booked_Seats':tkt['userticket']['Number_Of_Passengers'],
#               'remaining_Seats':train_data.total_seats_train-tkt['userticket']['Number_Of_Passengers'],
#             }
#         booked_tickets=SeatAvailDB.objects.create(**temp)
#         return HttpResponse("seat created!")

@api_view(['GET','POST'])
def Seat(request,tkt):
    # print(tkt['userticket'])
    ticket_details=SeatAvailDB.objects.filter(ticket_date=tkt['Boarding_Date'],train_number=tkt['Train_Number'])
    train_data=TrainData.objects.get(trainNumber=tkt['Train_Number'])
    # print("ticket_details::",ticket_details)
    if ticket_details:
        booked_tickets=SeatAvailDB.objects.get(ticket_date=tkt['Boarding_Date'],train_number=tkt['Train_Number'])
        bs=booked_tickets.booked_Seats
        # print("bs::",bs)
        booked_tickets.booked_Seats=bs+tkt['Number_Of_Passengers']
        print("new pas num::",tkt['Number_Of_Passengers'])
        booked_tickets.total_seats=train_data.total_seats_train
        booked_tickets.remaining_Seats=booked_tickets.total_seats- booked_tickets.booked_Seats
        booked_tickets.save()
        return "seat created!"
    else:
        temp={'ticket_date':tkt['Boarding_Date'],
              'train_number':tkt['Train_Number'],
              'total_seats':train_data.total_seats_train,
              'booked_Seats':tkt['Number_Of_Passengers'],
              'remaining_Seats':train_data.total_seats_train-tkt['Number_Of_Passengers'],
            }
        booked_tickets=SeatAvailDB.objects.create(**temp)
        return "seat created!"