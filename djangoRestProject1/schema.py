import graphene
from graphene_django import DjangoObjectType
from userapp.models import AppUser
from messageapp.models import Message
from todoapp.models import Project, ToDo


class UserType(DjangoObjectType):  # А-ля формы или сериализаторы для моделей
    class Meta:
        model = AppUser

    fields = '__all__'


class ProjectType(DjangoObjectType):  # А-ля формы или сериализаторы для моделей
    class Meta:
        model = Project

    fields = '__all__'


class MessageType(DjangoObjectType):  # А-ля формы или сериализаторы для моделей
    class Meta:
        model = Message

    fields = '__all__'


class TodoType(DjangoObjectType):  # А-ля формы или сериализаторы для моделей
    class Meta:
        model = ToDo

    fields = '__all__'


class MessageTextMutationByUid(graphene.Mutation):
    class Arguments:
        text = graphene.String(required=True)
        message_uid = graphene.UUID(required=True)
    message = graphene.Field(MessageType)

    @classmethod
    def mutate(cls, root, info, text, message_uid):
        message = Message.objects.get(uid=message_uid)
        message.text = text
        message.save()
        return MessageTextMutationByUid(message=message)


class Mutation(graphene.ObjectType):
    update_message = MessageTextMutationByUid.Field()


class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)  # Тут определяем поля схемы
    all_projects = graphene.List(ProjectType)
    all_messages = graphene.List(MessageType)
    all_todos = graphene.List(TodoType)
    user_by_username = graphene.Field(UserType, username=graphene.String(required=True))
    messages_by_sender_username = graphene.List(MessageType, username=graphene.String(required=False))

    def resolve_all_users(root, info):  # определяем метод получения поля
        return AppUser.objects.all()

    def resolve_all_projects(root, info):  # определяем метод получения поля
        return Project.objects.all()

    def resolve_all_messages(root, info):  # определяем метод получения поля
        return Message.objects.all()

    def resolve_all_todos(root, info):  # определяем метод получения поля
        return ToDo.objects.all()

    def resolve_user_by_username(self, info, username):
        try:
            return AppUser.objects.get(user_name=username)
        except AppUser.DoesNotExist:
            return None

    def resolve_messages_by_sender_username(self, info, username=None):
        messages = Message.objects.all()
        if username:
            messages = Message.objects.filter(sender__user_name=username)
        return messages


schema = graphene.Schema(query=Query, mutation=Mutation)
