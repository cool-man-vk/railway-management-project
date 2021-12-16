from django import forms  
from .models import *
from django.forms import widgets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

    
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactDetail 
        fields = "__all__" 

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            
class TrainDetailsForm(forms.ModelForm):
    class Meta:
        model = TrainModels
        fields = "__all__" 
        
class BookingForm(forms.ModelForm): 
    class Meta:
        model = Train_booking_Model
        fields = [ 'name' , 'age' , 'date_of_birth' ,'trainName', 'no_of_persons' , 'aadhar_number' , 
                  'type_of_coach' , 'date'  ,'place'] 
        
class PersonsForm(forms.ModelForm):
    class Meta:
        model = PersonsDetailsModel 
        fields = "__all__" 