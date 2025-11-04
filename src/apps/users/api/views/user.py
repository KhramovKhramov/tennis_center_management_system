from apps.users.api.serializers import UserSerializer
from apps.users.models import User
from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    """API для работы с пользователями."""

    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
