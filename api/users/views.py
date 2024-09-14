from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import User
from .serializer import UserSerializer
from rest_framework import generics

# Create your views here.
#user by id - get, update,delete
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#get users
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# hello world
def helloWorld(request):
    return HttpResponse("Hello, World!")

