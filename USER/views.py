from django.http import HttpResponse,JsonResponse
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from SEATAVAIL.views import Seat
class UserView(viewsets.ModelViewSet):
    queryset=UserDB.objects.all()
    serializer_class=UserDBSerializer

@api_view(['POST','DELETE'])    
def CreateTicket(request):
    if request.method=='POST':
        user_mobile=request.data.pop('Mobile_Number')
        userticket=request.data.pop("userticket")
        user=UserDB.objects.filter(Mobile_Number=user_mobile)
        if user:
            user_details=UserDB.objects.get(Mobile_Number=user_mobile)
            passenger=userticket.pop('passenger')
            ticket=TicketDB.objects.create(User_Mobile=user_details,**userticket)
            for p in passenger:
                psd=p.pop('passenger_seat_details')
                passenger_object=PassengerDB.objects.create(ticket_id=ticket,**p)
                PassengerSeatDB.objects.create(passenger_id=passenger_object,**psd)
            return HttpResponse("ticket created!")
        else:
            return HttpResponse("user not reg register first!")
    # if request.method=='DELETE':
    #     d=TicketDB.objects.filter(Journey_From="chennai")
    #     for i in d:
    #         i.delete()
    #     return JsonResponse("data deleted!",safe=False)
    
def getpnr(request,pnr_no):
    print("pnr::",pnr_no)
    t=TicketDB.objects.filter(PNR_Number=pnr_no)
    if t:
        a=TicketDB.objects.get(PNR_Number=pnr_no)
        s=TicketDBSerializer(a)
        return JsonResponse(s.data,safe=False)
    else:
        return HttpResponse("pnr_number not exist!")