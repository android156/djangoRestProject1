from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from messageapp.models import Message
from messageapp.serializers import MessageModelSerializer


class MessageModelViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageModelSerializer
