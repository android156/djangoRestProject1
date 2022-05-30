from django.shortcuts import render
from rest_framework import mixins, viewsets
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet
from .models import AppUser
from .serializers import UserModelSerializerAll
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny

data = {
    'title': '',
    'h1': '',
    'users': []
}


class AppUserModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    queryset = AppUser.objects.all()
    serializer_class = UserModelSerializerAll


class AppUserListUpdateViewSet(mixins.UpdateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                               viewsets.GenericViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    queryset = AppUser.objects.all()
    serializer_class = UserModelSerializerAll


def start_page(request):
    data['title'] = 'TODO'
    data['h1'] = 'Web-сервис для работы с TODO-заметками'
    return render(request, 'mainapp/start_page.html', context=data)
