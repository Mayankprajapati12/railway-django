from django.db import models

class UserDB(models.Model):
    New=models.CharField(max_length=50)
    Email=models.EmailField(unique=True)
    Mobile_Number=models.IntegerField(unique=True)
    Password=models.CharField(unique=True,max_length=10)