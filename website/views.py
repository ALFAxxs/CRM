from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    #check to see if logging in
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect('home')
        else:
            messages.success(request, "There was an error Logging in , Please try again!")
    return render(request, 'home.html', {})


def register_user(request):
    return render(request, 'registration.html', {})


def login_user(request):
    pass


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out!")
    return redirect('home')