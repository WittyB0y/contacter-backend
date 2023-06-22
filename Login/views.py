from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics, permissions, status

from .serializers import UserGetTokenSerializer


class ObtainTokenView(generics.CreateAPIView):
    serializer_class = UserGetTokenSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs) -> Response:
        """Return AuthToken"""
        username = request.data.get('username')
        password = request.data.get('password')

        if username is None or password is None:
            return Response({'error': 'Please provide both username and password.'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)

        if not user:
            return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)
        token = str(refresh.access_token)

        return Response({'token': token})
