from rest_framework.viewsets import ModelViewSet
from .models import AppUser
from .serializers import UserModelSerializer


class AuthorModelViewSet(ModelViewSet):
    queryset = AppUser.objects.all()
    serializer_class = UserModelSerializer
