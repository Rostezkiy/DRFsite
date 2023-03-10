from django.shortcuts import render
from rest_framework import generics
from .models import Device
from .serializers import *


class DeviceAPIView(generics.ListAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
