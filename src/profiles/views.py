from .models import UserNet
from .serializers import GetUserNetSerializer, GetUserNetPublicSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions


class UserNetPublicView(ModelViewSet):
    """View user's public profile"""
    queryset = UserNet.objects.all()
    serializer_class = GetUserNetPublicSerializer
    permission_classes = [permissions.AllowAny]


class UserNetView(ModelViewSet):
    """View user's profile"""

    serializer_class = GetUserNetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserNet.objects.filter(id=self.request.user.id)
