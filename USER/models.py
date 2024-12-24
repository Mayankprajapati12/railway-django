from django.db import models

class UserDB(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.EmailField(unique=True)
    Mobile_Number=models.IntegerField(unique=True)
    Password=models.CharField(unique=True,max_length=10)
  
class TicketDB(models.Model):
    User_Mobile=models.ForeignKey(UserDB,to_field='Mobile_Number',on_delete=models.CASCADE,related_name='userticket')
    PNR_Number=models.AutoField(primary_key=True)
    Journey_From=models.CharField(max_length=50)
    Journey_To=models.CharField(max_length=50)
    Boarding_Date=models.DateField(null=True,blank=True)
    Boarding_Time=models.CharField(max_length=10)
    Boarding_Station=models.CharField(max_length=50)
    Destination_Arrival_Date=models.DateField(null=True,blank=True)
    Destination_Arrival_Time=models.CharField(max_length=10)
    Journey_Distance=models.IntegerField(null=True,blank=True)
    Train_Number=models.IntegerField(null=True,blank=True)
    Train_Name=models.CharField(max_length=50)
    Seat_Quota=models.CharField(max_length=10)
    Coach_Class=models.CharField(max_length=20)
    Booking_Date=models.DateField(null=True,blank=True)
    Number_Of_Passengers=models.IntegerField(null=True,blank=True)
    Ticket_Price=models.IntegerField(null=True,blank=True)
    Ticket_Status=models.CharField(max_length=10) # CNF | WL | RAC
    Journey_Status=models.CharField(max_length=20) # Completed | Pending | Cancelled
    
class PassengerDB(models.Model):
    ticket_id=models.ForeignKey(TicketDB,on_delete=models.CASCADE,related_name='passenger')
    Passenger_Name=models.CharField(max_length=50)
    Passenger_Age=models.IntegerField()
    Passenger_Gender=models.CharField(max_length=10)
    
class PassengerSeatDB(models.Model):
    passenger_id=models.OneToOneField(PassengerDB,on_delete=models.CASCADE,related_name='passenger_seat_details')
    Booking_Status=models.CharField(max_length=50)
    Current_Status=models.CharField(max_length=50)
    Berth_Coach=models.CharField(max_length=50,null=True,blank=True)
    Berth_Number=models.IntegerField(null=True,blank=True)
    Berth_Type=models.CharField(max_length=5,null=True,blank=True)