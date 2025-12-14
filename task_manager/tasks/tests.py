from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Task

User = get_user_model()


class TaskAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", email="test@example.com", password="password123"
        )
        self.client.login(username="testuser", password="password123")

    def test_create_task(self):
        url = reverse("task-list")
        data = {
            "title": "Sample Task",
            "description": "Test desc",
            "due_date": (timezone.now() + timezone.timedelta(days=1)).isoformat(),
            "priority": Task.PRIORITY_HIGH,
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)

    def test_owner_only_access(self):
        task = Task.objects.create(
            owner=self.user,
            title="Private Task",
            description="",
            due_date=timezone.now() + timezone.timedelta(days=1),
        )
        other = User.objects.create_user(
            username="other", email="other@example.com", password="password123"
        )
        self.client.logout()
        self.client.login(username="other", password="password123")
        url = reverse("task-detail", args=[task.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_mark_complete_and_edit(self):
        task = Task.objects.create(
            owner=self.user,
            title="Task",
            description="",
            due_date=timezone.now() + timezone.timedelta(days=1),
        )
        complete_url = reverse("task-complete", args=[task.id])
        response = self.client.post(complete_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        task.refresh_from_db()
        self.assertEqual(task.status, Task.STATUS_COMPLETED)
        update_url = reverse("task-detail", args=[task.id])
        response = self.client.patch(update_url, {"title": "New"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        incomplete_url = reverse("task-incomplete", args=[task.id])
        response = self.client.post(incomplete_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
