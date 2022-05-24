from django.shortcuts import render
from rest_framework import mixins, viewsets
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet
from .models import AppUser
from .serializers import UserModelSerializerAll

data = {
    'title': '',
    'h1': '',
    'users': []
}


class AppUserModelViewSet(ModelViewSet):

    queryset = AppUser.objects.all()
    serializer_class = UserModelSerializerAll


class AppUserListUpdateViewSet(mixins.UpdateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                               viewsets.GenericViewSet):
    queryset = AppUser.objects.all()
    serializer_class = UserModelSerializerAll


def start_page(request):
    data['title'] = 'TODO'
    data['h1'] = 'Web-сервис для работы с TODO-заметками'
    return render(request, 'mainapp/start_page.html', context=data)
