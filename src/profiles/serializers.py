from rest_framework import serializers
from .models import UserNet


class GetUserNetSerializer(serializers.ModelSerializer):
    """Export info about User"""

    avatar = serializers.ImageField(write_only=True)

    class Meta:
        model = UserNet
        exclude = ('groups',
                   'user_permissions',
                   'password',
                   'last_login',
                   'is_active',
                   'is_staff',
                   'is_superuser',
                   )


class GetUserNetPublicSerializer(serializers.ModelSerializer):
    """Export public info about User"""

    avatar = serializers.ImageField(read_only=True)

    class Meta:
        model = UserNet
        exclude = ('groups',
                   'user_permissions',
                   'email',
                   'password',
                   'last_login',
                   'is_active',
                   'is_staff',
                   'is_superuser',
                   )


class UserFollowerSerializer(serializers.ModelSerializer):

    avatar = serializers.ImageField(read_only=True)

    class Meta:
        model = UserNet
        fields = ('id', 'username', 'avatar')
