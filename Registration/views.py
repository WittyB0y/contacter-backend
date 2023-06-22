from django.contrib.auth.models import User
from rest_framework import generics, permissions

from .serializers import UserSerializer


class RegisterView(generics.CreateAPIView):
    """Create API for registration user"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(serializer.validated_data['password'])
        user.save()
