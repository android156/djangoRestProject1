from rest_framework.generics import CreateAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from todoapp.filters import ProjectFilter, ToDoFilter
from todoapp.models import Project, ToDo
from todoapp.serializers import ProjectModelSerializerAll, ToDoModelSerializer, ToDoModelSerializerForApiView, \
    ProjectModelSerializerBaseAll, ToDoModelSerializerBase


class ToDoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializerAll


class ToDoModelViewSet(ModelViewSet):
    # permission_classes = [IsAuthenticated, ]
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer
    # filterset_class = ToDoFilter

    def get_serializer_class(self):

        if self.request.method in ['GET']:
            return ToDoModelSerializer
        return ToDoModelSerializerBase

    pagination_class = ToDoLimitOffsetPagination

    # Переопределили удаление.
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()


class MyApiView(APIView):
    # permission_classes = [AllowAny,]

    # renderer_classes = [JSONRenderer]
    def get(self, request):
        todos = ToDo.objects.all()
        serializer = ToDoModelSerializerForApiView(todos, many=True)
        return Response(serializer.data)

    def post(self, request):
        return Response('POST SUCCESS')


class ProjectCreateAPIView(CreateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializerAll


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ProjectLimitOffsetPaginationViewSet(ModelViewSet):
    # для тестов отключили permissions
    # permission_classes = [IsAuthenticated, ]


    queryset = Project.objects.all()

    serializer_class = ProjectModelSerializerAll
    # для тестов отключили pagination
    # pagination_class = ProjectLimitOffsetPagination
    filterset_class = ProjectFilter

    # def get_serializer_class(self):
    #     if self.request.method in ['GET']:
    #         return ProjectModelSerializerAll
    #     return ProjectModelSerializerBaseAll
    #
