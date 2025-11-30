from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated", "IsAuthenticated
from django.urls import path
from .views import (
    BookListView,
    BookCreateView,
    BookDetailView,
    BookUpdateView,
    BookDeleteView
)

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/update/', BookUpdateView.as_view(), name='book-update'),  # Unusual path for updating
    path('books/delete/', BookDeleteView.as_view(), name='book-delete'),  # Unusual path for deleting
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-pk-update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-pk-delete'),
]
