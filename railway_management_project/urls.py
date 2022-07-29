"""railway_management_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages.views import *

handler500 = 'pages.views.error500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage,name='homepage'),
    path('login/',login,name='login'),
    path('signup/',signup,name='signup'),
    path('dashboard/',dashboard_page,name="dashboard page"),
    path('book_trains/',book_trains_page,name='booking page'),
    path('logout/',logoutPage,name='logoutPage'),
    path('booking_lists/',TrainBookedlist,name='Train Booking List')
]
