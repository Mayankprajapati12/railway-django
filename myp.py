# # totalseats=480
# # seatspercoach=80
# # coaches=6
# # bookedseats=337
# # remainingseats=totalseats-bookedseats
# # c=bookedseats//seatspercoach
# # t=seatspercoach*c
# # a=bookedseats-t
# # print(a)
# coaches=[
#             {
#                 "coach_class": "sleeper",
#                 "coach_class_code": "S",
#                 "number_of_coaches": 5,
#                 "seats_per_coach": 80,
#                 "price_per_km": 0.46,
#                 "coach_seat_detail": 
#                     {
#                         "general_seats": 51,
#                         "tatkal_seats": 16,
#                         "ladies_seats": 6,
#                         "senior_citizen_lowerberth_seats": 7
#                     }
                
#             },
#             {
#                 "coach_class": "thirdac",
#                 "coach_class_code": "B",
#                 "number_of_coaches": 5,
#                 "seats_per_coach": 72,
#                 "price_per_km": 1.1960000000000002,
#                 "coach_seat_detail": 
#                     {
#                         "general_seats": 52,
#                         "tatkal_seats": 16,
#                         "ladies_seats": None,
#                         "senior_citizen_lowerberth_seats": 4
#                     }
                
#             },
#             {
#                 "coach_class": "secondac",
#                 "coach_class_code": "A",
#                 "number_of_coaches": 3,
#                 "seats_per_coach": 54,
#                 "price_per_km": 1.748,
#                 "coach_seat_detail": 
#                     {
#                         "general_seats": 40,
#                         "tatkal_seats": 10,
#                         "ladies_seats": None,
#                         "senior_citizen_lowerberth_seats": 4
#                     }
                
#             },
#             {
#                 "coach_class": "first_ac",
#                 "coach_class_code": "H",
#                 "number_of_coaches": 3,
#                 "seats_per_coach": 24,
#                 "price_per_km": 2.9440000000000004,
#                 "coach_seat_detail": 
#                     {
#                         "general_seats": 24,
#                         "tatkal_seats": None,
#                         "ladies_seats": None,
#                         "senior_citizen_lowerberth_seats": None
#                     }
                
#             }
#         ]
# s=0
# for i in coaches:
#     total=i['seats_per_coach']*i['number_of_coaches']
#     print(total)
#     s=s+total
# print(s)

# from datetime import datetime,time
# timea=datetime.now()
# # sp=datetime(2025,1,13).date()
# # cp=timea.date()
# # if sp < cp:
# #     print("before 15")
# # else:
# #     print("after 15")
# ct=timea.time()
# x=time(20,31,0)
# # print(ct)
# # print(x)
# def tt():
#     with open("modeltest.py","r") as j:
#         c=j.readlines()
#     c[3]=c[3].replace("City","New")
#     # print(e)
#     with open("modeltest.py","w") as f:
#         f.writelines(c)

# if ct>=x:
#     tt()
# else:
#     print("wait...")
# def updatemodel(dt):
#     with open("Train/SEATAVAIL/models.py", "r") as d:
#         c=d.readlines()

#     with open("Train/SEATAVAIL/models.py","w") as o:
#         for l in c:
#             if dt not in l:
#                 o.write(l)

#     with open("Train/SEATAVAIL/models.py","a") as a:
#         a.write("jan6=models.JSONField(null=True)")
    
# updatemodel("jan3")x  


from datetime import datetime, timedelta
import schedule
import time
import django
import os
from django.core.management import call_command
def updatemodel(dt):
    print("on time !!")
    with open("Train/SEATAVAIL/models.py", "r") as d:
        c=d.readlines()

    with open("Train/SEATAVAIL/models.py","w") as o:
        for l in c:
            if dt not in l:
                o.write(l)

    last_date=(datetime.today().date()+timedelta(days=5)).strftime("%b%d")

    with open("Train/SEATAVAIL/models.py","a") as a:
        a.write(f"\n   {last_date}=models.JSONField(null=True)")

    os.environ.setdefault('DJANGO_SETTINGS_MODULE','Train.settings')
    # settings.configure(default_settings=prj.settings)
    django.setup()
    call_command('makemigrations','SEATAVAIL','--noinput')
    call_command('migrate','SEATAVAIL','--noinput')

c=datetime.now()
previoustwodate=(datetime.today().date()+timedelta(days=-2)).strftime("%b%d")
schedule.every().day.at("19:46:00").do(lambda: updatemodel(previoustwodate))
while True:
    schedule.run_pending()
    time.sleep(1)