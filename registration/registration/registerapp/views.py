from django.shortcuts import render
from rest_framework import generics
from .serializers import RegisterCreateSerializer, RegisterListSerializer
from .models import RegisterUser


class RegisterCreateView(generics.CreateAPIView):
    """ Registration create view """

    queryset = RegisterUser.objects.all()
    serializer_class = RegisterCreateSerializer


class RegisterListView(generics.ListAPIView):
    """ Registered users list view """

    queryset = RegisterUser.objects.all()
    serializer_class = RegisterListSerializer
