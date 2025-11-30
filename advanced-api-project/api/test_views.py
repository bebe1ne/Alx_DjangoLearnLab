from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Author, Book

class BookAPITests(APITestCase):

    def setUp(self):
        self.author = Author.objects.create(name="Test Author")
        self.book = Book.objects.create(title="Test Book", publication_year=2020, author=self.author)
    
    def test_create_book(self):
        url = reverse('book-list')
        data = {'title': 'New Book', 'publication_year': 2021, 'author': self.author.id}
        response = self.client.post(url, data, format='json')
        # Status code check
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Response data check
        self.assertEqual(response.data['title'], 'New Book')

    def test_get_books(self):
        url = reverse('book-list')
        response = self.client.get(url, format='json')
        # Status code check
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Response data check
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Test Book")

    def test_get_book_detail(self):
        url = reverse('book-detail', kwargs={'pk': self.book.pk})
        response = self.client.get(url, format='json')
        # Status code check
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Response data check
        self.assertEqual(response.data['title'], "Test Book")

    def test_update_book(self):
        url = reverse('book-detail', kwargs={'pk': self.book.pk})
        data = {'title': 'Updated Book'}
        response = self.client.patch(url, data, format='json')
        # Status code check
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Response data check
        self.assertEqual(response.data['title'], 'Updated Book')

    def test_delete_book(self):
        url = reverse('book-detail', kwargs={'pk': self.book.pk})
        response = self.client.delete(url)
        # Status code check
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Confirm the book no longer exists
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
