from rest_framework import generics, viewsets, routers

from .serializers import *


class DevicesViewset(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
