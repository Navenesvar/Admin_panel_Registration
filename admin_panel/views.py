from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth.models import User
from django.contrib import messages
from telnetlib import LOGOUT
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError


# Create your views here.
def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        name = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 == password2:
            try:
                user = User.objects.create_user(username=name, email=email, password=password1)
                user.is_staff = True
                user.is_superuser = True
                user.save()
                messages.success(request, 'Your account has been created! You are able to login')
                return redirect('Login')
            except IntegrityError:
                messages.warning(request, 'Username is already taken. Please choose a different username.')
                return redirect('Register')
        else:
            messages.warning(request, 'Passwords do not match.')
            return redirect('Register')

    else:
        form = CreateUserForm()
        return render(request, "register.html", {'form': form})
@login_required
def profile(request):
    return render(request,'profile.html')
def logout(request):
    username = UserLoggedIn(request)
    if username != None:
        LOGOUT(request)
        return redirect('Home')
def UserLoggedIn(request):
    if request.user.is_authenticated == True:
        username = request.user.username
    else:
        username = None
    return username