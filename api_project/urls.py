Main urls.py
# api_project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Include the app's urls
]
Authentication Token Endpoint (optional setup in views.py for obtain_auth_token)
# Adding obtain_auth_token in `api/urls.py`

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns += [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
