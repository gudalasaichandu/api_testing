from django.shortcuts import render
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateAPIView
)
from main import models, serializers
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class ListView(ListCreateAPIView):
    #permission_classes = (IsAuthenticated,)
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer

class UpdateApiView(RetrieveUpdateAPIView):
    #permission_classes = (IsAuthenticated,)
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer


class filtering(ListCreateAPIView):
    #permission_classes = (IsAuthenticated,)
    queryset = models.Student.objects.filter(name__icontains='S')
    serializer_class = serializers.StudentSerializer
