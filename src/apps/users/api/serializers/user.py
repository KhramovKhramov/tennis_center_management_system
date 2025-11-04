from apps.users.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор данных пользователя."""

    class Meta:
        model = User
        fields = (
            'id',
            'last_name',
            'first_name',
            'patronymic',
            'username',
            'date_of_birth',
            'gender',
            'email',
            'phone_number',
            'password',
        )
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def save(self, **kwargs):
        password = self.validated_data.get('password')
        # TODO пусть пароль генерируется автоматически
        if password:
            self.validated_data['password'] = make_password(password)

        return super().save(**kwargs)
