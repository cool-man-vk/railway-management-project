from django.db import models
from django.utils import timezone 
from datetime import datetime
from django.contrib.auth.models import User

choice = (
    ('a','3ac'), 
    ('b','2ac'), 
    ('c','1ac')
)
# Create your models here.
class TrainModels(models.Model):
    train_number = models.IntegerField()
    train_name = models.CharField(max_length=50)
    from_date = models.DateField(auto_now_add=False)  
    end_date = models.DateField(auto_now=False) 
    coaches = models.CharField(max_length = 10,choices = choice)
    arrival_time = models.DateTimeField(default= timezone.now) 
    departure_time = models.DateTimeField(default= timezone.now) 
    source_station = models.CharField(max_length=45) 
    dest_station = models.CharField(max_length=50) 
    
    def __str__(self):
        return self.train_name
    
class ContactDetail(models.Model):  
    name = models.CharField(max_length=50) 
    email = models.EmailField() 
    subject = models.CharField(max_length=100) 
    message = models.TextField(max_length=350) 
    
    def __str__(self): 
        return self.name 
    
class Train_booking_Model(models.Model):
    user= models.ForeignKey(User, on_delete = models.CASCADE,null=True)
    name = models.CharField(max_length=100) 
    age = models.IntegerField() 
    date_of_birth = models.DateField(auto_now_add=False)
    no_of_persons = models.IntegerField()  
    aadhar_number = models.BigIntegerField() 
    type_of_coach = models.CharField(max_length=10,choices = choice) 
    date = models.DateField(auto_now_add=False) 
    trainName = models.ForeignKey(TrainModels,on_delete=models.CASCADE,null=False,related_name="trainName")
    place = models.CharField(max_length = 25)  
    
class PersonsDetailsModel(models.Model):
    name = models.CharField(max_length=200) 
    age = models.IntegerField()  
    date_of_birth = models.DateField(default=datetime.now) 
    

     
    