from django.shortcuts import render
from rest_framework import generics
from .serializers import RegisterSerializer, SerializerList
from .models import RegisterUser


class RegisterAPIView(generics.CreateAPIView):
    """registration create view"""

    queryset = RegisterUser.objects.all()
    serializer_class = RegisterSerializer


class RegisterListAPIView(generics.ListAPIView):
    queryset = RegisterUser.objects.all()
    serializer_class = SerializerList
