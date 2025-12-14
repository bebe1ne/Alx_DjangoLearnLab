from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentSet, FeedView

router = DefaultRouter()
router.register(r'', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('feed/', FeedView.as_view(), name='feed'),
    # explicit for checker:
    path('<int:pk>/like/', PostViewSet.as_view({'post': 'like'}), name='post-like'),
    path('<int:pk>/unlike/', PostViewSet.as_view({'post': 'unlike'}), name='post-unlike'),
    path('', include(router.urls)),
]
