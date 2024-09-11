from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import UserDetails


def hello_world(request):
    return HttpResponse("Hello, world!")


def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if the email is unique
        if UserDetails.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('signup')

        # Create a new user
        new_user = UserDetails(username=username, email=email, password=password)
        new_user.save()

        messages.success(request, "Signup successful! Please log in.")
        return redirect('login')

    return render(request, 'signup.html')



def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if the user exists and password matches
        try:
            user = UserDetails.objects.get(email=email)
            if user.password == password:
                messages.success(request, f"Welcome {user.username}!")
                return render(request, 'success.html')
            else:
                messages.error(request, "Incorrect password")
        except UserDetails.DoesNotExist:
            messages.error(request, "User does not exist")

    return render(request, 'login.html')