from django_filters import rest_framework as filters
from .models import Project, ToDo


class ProjectFilter(filters.FilterSet):
    class Meta:
        model = Project
        fields = ['name', 'description']
    name = filters.CharFilter(lookup_expr='contains')
    description = filters.CharFilter(lookup_expr='contains')


class ToDoFilter(filters.FilterSet):
    class Meta:
        model = ToDo
        fields = ['user', 'is_active', 'text']
    text = filters.CharFilter(lookup_expr='contains')
