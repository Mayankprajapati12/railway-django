from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(UserDB)
admin.site.register(TicketDB)
admin.site.register(PassengerDB)
admin.site.register(PassengerSeatDB)