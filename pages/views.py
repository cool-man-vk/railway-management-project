from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *
from django.db.models import Q
from django.shortcuts import render , redirect 
from django.http import HttpResponse 
from django.contrib import messages 
from django.contrib.auth import authenticate , logout , login  as auth_login 
from django.contrib.auth.decorators import login_required

def homepage(request):
    form = ContactForm(request.POST or None)  
    if form.is_valid():
            form.save() 
            form = ContactForm() 
            
    context = {'form': form}
    return render(request, 'pages/index.html',context) 

def login(request):
        if request.user.is_authenticated:
            return redirect('/dashboard/')
        if request.method == 'POST':
            username = request.POST.get('usname') 
            password = request.POST.get('password') 

            user = authenticate(request , username = username, password = password) 

            if user is not None:
                    auth_login(request,user) 
                    return redirect('/dashboard/') 
            else:
                    messages.info(request,'Username or password is incorrect')
                    return redirect('/login/')
        return render(request, 'pages/login.html') 
    
def signup(request):
    if request.user.is_authenticated:
            return redirect('/dashboard/')
    else:
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            messages.success(request, f'Your account has been created ! You will be now able to log in')
            return render(request,'pages/login.html')
        else:
            form = UserRegisterForm()
    return render(request, 'pages/signup.html', {'form': form, 'title':'reqister here'})

@login_required(login_url='login')
def dashboard_page(request):
    data = TrainModels.objects.all().values()
    train_exact_name = request.GET.get('train_name') 
    train_destination = request.GET.get('dest_station')
    if train_exact_name!= '' and train_exact_name is not None:
        data = data.filter(train_name__icontains = train_exact_name)
    elif train_destination!= '' and train_destination is not None:
        data = data.filter(dest_station__icontains = train_destination)
    elif train_exact_name!= '' and train_destination is not None:
        data = data.filter(Q(train_name__icontains = train_exact_name) | Q(dest_station__icontains = train_destination)).distinct()
    context = { 'data': data }
    return render(request,"pages/dashboard1.html",context) 

@login_required(login_url='login')
def book_trains_page(request):
    form = BookingForm(request.POST or None) 
    if request.POST:
        if form.is_valid():
            fs = form.save(commit=False)
            fs.user = request.user  
            fs.save() 
            form = BookingForm() 
    context = { 'form':form }
    return render(request,"pages/booking.html",context) 

def logoutPage(request):
    logout(request) 
    return redirect('login')

@login_required(login_url='login')
def TrainBookedlist(request):
    datas = Train_booking_Model.objects.filter(user=request.user).all().values()
    context = {'datas':datas}
    # context['trainName_id'] = trainName_id.values()
    return render(request,"pages/mybookings.html",context) 

def proceedPage(request):
    return render(request,"pages/proceed.html") 