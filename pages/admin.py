from django.contrib import admin

# Register your models here.
from .models import * 

# register
admin.site.register(TrainModels) 
admin.site.register(ContactDetail)
admin.site.register(Train_booking_Model)