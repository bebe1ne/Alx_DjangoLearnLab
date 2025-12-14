
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from accounts.models import User
from .models import Notification

class NotificationTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='u1', password='pass1234')
        self.client.force_authenticate(self.user)

    def test_empty_notifications(self):
        url = reverse('notifications-list')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data['results']) if isinstance(resp.data, dict) and 'results' in resp.data else len(resp.data), 0)
