from rest_framework import serializers
from ..profiles.serializers import UserFollowerSerializer
from .models import Follower


class ListFollowerSerializer(serializers.ModelSerializer):

    subscriber = UserFollowerSerializer(many=True, read_only=True)

    class Meta:
        model = Follower
        fields = ('subscriber',)
