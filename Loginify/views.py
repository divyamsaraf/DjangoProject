import json
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import UserDetailsSerializer
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
            return redirect('Loginify/signup')

        # Create a new user
        new_user = UserDetails(username=username, email=email, password=password)
        new_user.save()

        messages.success(request, "Signup successful! Please log in.")
        return redirect('login')

    return render(request, 'Loginify/signup.html')



def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = UserDetails.objects.get(email=email)
            if user.password == password:
                messages.success(request, f"Welcome {user.username}!")
                return render(request, 'Loginify/success.html')
            else:
                messages.error(request, "Incorrect password")
        except UserDetails.DoesNotExist:
            messages.error(request, "User does not exist")

    return render(request, 'Loginify/login.html')



@api_view(['GET'])
def get_all_users(request):
    if request.method == 'GET':
        try:
            all_users = UserDetails.objects.all()
            serializer_data = UserDetailsSerializer(all_users, many=True)
            return JsonResponse(serializer_data.data, safe=False)
        except Exception as e:
            return JsonResponse({"error": str(e)})
        


@api_view(['GET'])
def get_user_by_email(request, email):
    if request.method == 'GET':
        try:
            user_by_email = UserDetails.objects.get(email=email)
            serializer_data = UserDetailsSerializer(user_by_email)
            return JsonResponse(serializer_data.data, safe=False)
        except UserDetails.DoesNotExist:
                    return Response({'error': 'User not found'}, status=404)




@api_view(['PUT'])
def update_user(request, id):
    if request.method == 'PUT':
        try:
            user_data = UserDetails.objects.get(id=id)
            input_data= json.loads(request.body)
            serializer_data = UserDetailsSerializer(user_data, data=input_data)
            if serializer_data.is_valid():
                serializer_data.save()
                return JsonResponse({'message': 'User data updated successfully'}, status=200)
            else:
                return JsonResponse(serializer_data.errors, status=400)
        except UserDetails.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)




@api_view(['PATCH'])
def partial_update_user(request, id):
    if request.method == 'PATCH':
        try:
            user_data = UserDetails.objects.get(id=id)
            input_data= json.loads(request.body)
            serializer_data = UserDetailsSerializer(user_data, data=input_data, partial=True)
            if serializer_data.is_valid():
                serializer_data.save()
                return JsonResponse({'message': 'User data updated successfully'}, status=200)
            else:
                return JsonResponse(serializer_data.errors, status=400)
        except UserDetails.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)




@api_view(['DELETE'])
def delete_user(request, id):
    if request.method == 'DELETE':
        try:
            user_data = UserDetails.objects.get(id=id)
            user_data.delete()
            return JsonResponse({'message': 'User deleted successfully'}, status=204)
        except UserDetails.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)