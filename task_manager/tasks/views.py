from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from rest_framework import viewsets, generics, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .filters import TaskFilter
from .models import Task
from .permissions import IsOwner
from .serializers import (
    TaskSerializer,
    UserRegisterSerializer,
    UserSerializer,
)

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserRegisterSerializer


class LoginView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserRegisterSerializer  # not actually used for response

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)
        if not user:
            return Response(
                {"detail": "Invalid credentials."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        login(request, user)
        return Response({"detail": "Logged in successfully."})


class MeUserView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    filterset_class = TaskFilter
    ordering_fields = ["due_date", "priority"]

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=True, methods=["post"])
    def complete(self, request, pk=None):
        task = self.get_object()
        if task.status == Task.STATUS_COMPLETED:
            return Response(
                {"detail": "Task is already completed."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        task.status = Task.STATUS_COMPLETED
        task.save()
        serializer = self.get_serializer(task)
        return Response(serializer.data)

    @action(detail=True, methods=["post"])
    def incomplete(self, request, pk=None):
        task = self.get_object()
        if task.status == Task.STATUS_PENDING:
            return Response(
                {"detail": "Task is already pending."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        task.status = Task.STATUS_PENDING
        task.save()
        serializer = self.get_serializer(task)
        return Response(serializer.data)
