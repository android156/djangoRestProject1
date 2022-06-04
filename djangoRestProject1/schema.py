import graphene
from graphene_django import DjangoObjectType
from userapp.models import AppUser
from messageapp.models import Message
from todoapp.models import Project, ToDo


class UserType(DjangoObjectType):
    class Meta:
        model = AppUser

    fields = '__all__'


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project

    fields = '__all__'


class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    all_projects = graphene.List(ProjectType)

    def resolve_all_users(root, info):
        return AppUser.objects.all()

    def resolve_all_projects(root, info):
        return Project.objects.all()


schema = graphene.Schema(query=Query)
