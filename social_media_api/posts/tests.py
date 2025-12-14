
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from accounts.models import User
from .models import Post

class PostsTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='u1', password='pass1234')
        self.client.force_authenticate(self.user)

    def test_create_post(self):
        url = reverse('post-list')
        resp = self.client.post(url, {"title": "Test", "content": "Body"}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
