from django.urls import path
from .views import (
    PostListView, PostDetailView, PostCreateView, PostUpdateView PostDeleteView,
   CreateView, CommentUpdateView, CommentDeleteView, register, profile, search
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:post_pk>/comments/new/', CommentCreateView.as_view(), name='comment_new'),  # For creating a new comment
    path('comment/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment_edit'),  # For editing a comment
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),  # For updating a comment
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),  # For deleting a comment
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logged_out.html'), name='logout'),
    path('profile/', profile, name='profile'),
    path('search/', search, name='search'),
]
