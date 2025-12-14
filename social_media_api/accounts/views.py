
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status, views
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from .models import User
from .serializers import (
    UserRegistrationSerializer,
    UserLoginSerializer,
    UserProfileSerializer,
)

class RegisterView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]

class LoginView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token = serializer.validated_data["token"]
        return Response(
            {"token": token, "user": UserProfileSerializer(user).data},
            status=status.HTTP_200_OK,
        )

class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        user_id = self.kwargs.get("pk")
        if user_id:
            return get_object_or_404(User, pk=user_id)
        return self.request.user

class FollowUserView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        target = get_object_or_404(User, pk=user_id)
        if target != request.user:
            target.followers.add(request.user)
        return Response(status=status.HTTP_204_NO_CONTENT)

class UnfollowUserView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        target = get_object_or_404(User, pk=user_id)
        if target != request.user:
            target.followers.remove(request.user)
        return Response(status=status.HTTP_204_NO_CONTENT)
