AUTH_USER_MODEL = 'relationship_app.CustomUser'
import os
from pathlib import Path

# Base directory setting
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings in production
DEBUG = False  # Ensure this is False in production to disable detailed error messages

ALLOWED_HOSTS = ['yourdomain.com']  # Replace with your domain

# Security and Privacy
SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key')  # Secure this key in production

# Security headers
SECURE_BROWSER_XSS_FILTER = True  # Helps prevent reflected XSS attacks
X_FRAME_OPTIONS = 'DENY'  # Prevents clickjacking attacks
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevents the browser from interpreting files as a different MIME type

# HTTPS settings
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True  # Ensures cookies are only sent over HTTPS
SECURE_SSL_REDIRECT = True  # Redirect all HTTP traffic to HTTPS

# Content Security Policy (CSP) settings
INSTALLED_APPS = [
    ...
    'csp',  # Add CSP middleware to help with security
]

MIDDLEWARE = [
    ...
    'csp.middleware.CSPMiddleware',  # Enable CSP middleware
]

CSP_DEFAULT_SRC = ("'self'",)
CSP_STYLE_SRC = ("'self'", 'fonts.googleapis.com',)
CSP_SCRIPT_SRC = ("'self'", 'apis.google.com',)