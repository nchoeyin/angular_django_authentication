from django.urls import path
from django import urls
from . views import UserDetail, UserList, helloWorld

urlpatterns = [
    path('users/', UserList.as_view(), name='User'),
    path('user/<int:pk>', UserDetail.as_view(), name='User'),
    path('hello', helloWorld, name='hello')
]