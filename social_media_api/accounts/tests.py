
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User

class AccountsTests(APITestCase):
    def test_register_and_login(self):
        url = reverse('register')
        data = {"username": "testuser", "email": "test@example.com", "password": "pass1234"}
        resp = self.client.post(url, data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        token = resp.data.get("token")
        self.assertIsNotNone(token)

        login_url = reverse('login')
        resp2 = self.client.post(login_url, {"username": "testuser", "password": "pass1234"}, format='json')
        self.assertEqual(resp2.status_code, status.HTTP_200_OK)
        self.assertIn("token", resp2.data)
