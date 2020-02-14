from django.shortcuts import render
from rest_framework import generics
import datetime
from django.utils import timezone

from .models import Content
from .serializers import ContentSerializer

# Create your views here.

class ContentInput(generics.ListCreateAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
