from rest_framework import generics

from .serializers import *


class DeviceAPIView(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class DeviceAPIUpdate(generics.UpdateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class DeviceAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
