from django.shortcuts import render, redirect   
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



def home(request):
    #Check to see if logging in
    if request.method == "POST":
        #Get the username and password
        username = request.POST["username"]
        password = request.POST["password"]
        #Check if the user is valid
        user = authenticate(request, username=username, password=password)
        if user is not None:
            #Log the user in
            login(request, user)
            messages.success(request, f"Welcome back, {username}!")
            return redirect("home")
        else:
            #Tell the user that the username or password is incorrect
            messages.error(request, "Invalid username or password.")
            return redirect("home")
    else:
        return render(request, "home.html", {})

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect("home")

def register_user(request):
    return render(request, "register.html", {})