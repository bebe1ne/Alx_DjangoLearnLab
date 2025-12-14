
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from tasks.views import TaskViewSet, RegisterView, MeUserView, LoginView

router = DefaultRouter()
router.register(r"tasks", TaskViewSet, basename="task")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/auth/register/", RegisterView.as_view(), name="register"),
    path("api/auth/login/", LoginView.as_view(), name="login"),
    path("api/users/me/", MeUserView.as_view(), name="me-user"),
    path("api-auth/", include("rest_framework.urls")),
]
