from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book, Author

class BookTests(APITestCase):
    def setUp(self):
        self.author = Author.objects.create(name="Test Author")
        self.book_url = reverse('book-list')

    def test_create_book(self):
        data = {"title": "New Book", "publication_year": 2023, "author": self.author.id}
        response = self.client.post(self.book_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_book(self):
        book = Book.objects.create(title="Existing Book", publication_year=2020, author=self.author)
        response = self.client.get(reverse('book-detail', args=[book.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
requirements.txt:
