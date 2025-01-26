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
