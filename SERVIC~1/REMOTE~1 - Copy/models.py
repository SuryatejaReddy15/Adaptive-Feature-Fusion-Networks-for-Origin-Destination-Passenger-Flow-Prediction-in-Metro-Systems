from django.db import models

# Create your models here.
from django.db.models import CASCADE


class ClientRegister_Model(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    gender= models.CharField(max_length=30)
    address= models.CharField(max_length=30)


class passenger_flow_prediction(models.Model):

    Fid= models.CharField(max_length=300)
    Tripid= models.CharField(max_length=300)
    Metro_Name= models.CharField(max_length=300)
    City= models.CharField(max_length=300)
    Source= models.CharField(max_length=300)
    Destination= models.CharField(max_length=300)
    Date_Time= models.CharField(max_length=300)
    NumberOfBoardings= models.CharField(max_length=300)
    Prediction= models.CharField(max_length=300)

class detection_accuracy(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)

class detection_ratio(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)



