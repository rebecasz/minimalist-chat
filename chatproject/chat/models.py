from django.db import models
from datetime import datetime
# Create your models here.
class Room(models.Model):
    name=models.CharField(max_length=20)

class Message(models.Model):
    value= models.CharField(max_length=100)
    date = models.DateField(default=datetime.now,blank=True)
    room=models.CharField(max_length=100)
    user=models.CharField(max_length=100)



