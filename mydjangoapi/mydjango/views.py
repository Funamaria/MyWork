from django.shortcuts import render
from rest_framework import generics
from .models import Content
from .serializers import ContentSerializer

# Create your views here.

class ContentInput(generics.ListCreateAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

class GoodsGet(generics.ListAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
