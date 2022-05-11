from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserModelSerializer


class AuthorModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
