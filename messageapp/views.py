from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from messageapp.models import Message
from messageapp.serializers import MessageModelSerializer, MessageModelSerializerAll


class MessageModelViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageModelSerializer

    def get_serializer_class(self):
        # if self.request.version == '0.2':   # namespacing
        # if self.request.version == '2.0':   # namespacing
        # if self.request.method in ['GET'] and self.request.version == '2.0.0':  #QueryParameterVersioning
        if self.request.version == '2.0.0':  # В заголовке Accept должно быть application/json; version=2.0.0
            return MessageModelSerializerAll
        return MessageModelSerializer

