from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import CustomUser

# Create your models here.



# Views

def signup(request):
    if request.method == 'POST':
        fname = request.POST.get('fname', '')
        lname = request.POST.get('lname', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        # Check if the user with the given email already exists
        if CustomUser.objects.filter(username=email).exists():
            messages.error(request, 'Account with this email already exists.')
            return redirect('/accounts/signup')

        # Create a new user
        new_user = CustomUser.objects.create_user(username=email, password=password)
        new_user.first_name = fname
        new_user.last_name = lname
        new_user.email = email
        new_user.amount = 2000.00
        new_user.save()

        messages.success(request, 'Account created successfully.')

        return redirect('/accounts/login/')
    else:
        return render(request, 'signup.html')


def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Bad Credentials!")
            return redirect('/accounts/login')
    else:
        return render(request, 'signin.html')

@login_required
def signout(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('/accounts/login')
