from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(TrainData)
admin.site.register(TrainCoaches)
admin.site.register(TrainStations)
admin.site.register(CoachQuota)