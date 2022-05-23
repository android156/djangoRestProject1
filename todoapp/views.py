from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from todoapp.models import Project, ToDo
from todoapp.serializers import ProjectModelSerializerAll, ToDoModelSerializer, ToDoModelSerializerForApiView


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializerAll


class ToDoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer


class MyApiView(APIView):

    # renderer_classes = [JSONRenderer]

    def get(self, request):
        todos = ToDo.objects.all()
        serializer = ToDoModelSerializerForApiView(todos, many=True)
        return Response(serializer.data)

    def post(self, request):
        return Response('POST SUCCESS')


class ArticleCreateAPIView(CreateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializerAll
