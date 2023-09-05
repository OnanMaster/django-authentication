from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm

# Create your views here.

def logout_view(request):
    if request.method == 'POST':
        
        logout(request)
        return redirect('/')
    
    return render(request,'logout.html')

def index(request):
    return render(request,'index.html')

def register(request):


    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('/')
    else:
        form = UserCreationForm()
     

    return render(request,'register.html',{'form':form})



def login_view(request):

    if request.method == "POST":
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            login(request,form.get_user())
            return redirect("/")
    else:
        form = AuthenticationForm()


   

    return render(request,'login.html',{'form':form})