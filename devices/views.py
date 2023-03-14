from rest_framework import generics, viewsets, routers
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import *
from .models import Category


class DevicesViewset(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

    @action(methods=['get'], detail=False)
    def categories_list(self, request):
        categories = Category.objects.all()
        return Response({'categories': [c.name for c in categories]})

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        categories = Category.objects.get(pk=pk)
        return Response({'category': categories.name})

    # return first N items, custom get_queryset
    # def get_queryset(self):
    #     pk = self.kwargs.get("pk")
    #
    #     if not pk:
    #         return Device.objects.all()[:3]
    #
    #     return Device.objects.filter(pk=pk)
