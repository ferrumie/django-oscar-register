from django.shortcuts import render
from rest_framework import generics
from .serializers import RegisterSerializer, SerializerList
from .models import RegisterUser


class RegisterAPIView(generics.CreateAPIView):
    """ Registration create view """

    queryset = RegisterUser.objects.all()
    serializer_class = RegisterSerializer


class RegisterListAPIView(generics.ListAPIView):
    """ Registered users list view """
    
    queryset = RegisterUser.objects.all()
    serializer_class = SerializerList
