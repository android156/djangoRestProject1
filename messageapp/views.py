from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from messageapp.models import Message
from messageapp.serializers import MessageModelSerializer, MessageModelSerializerAll


class MessageModelViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageModelSerializer

    def get_serializer_class(self):
        if self.request.version == '0.2':
            return MessageModelSerializerAll
        return MessageModelSerializer

