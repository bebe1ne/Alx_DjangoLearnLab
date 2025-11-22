AUTH_USER_MODEL = 'bookshelf.CustomUser'
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


# Ensure HTTPS is enforced
SECURE_SSL_REDIRECT = True  # Redirect all non-HTTPS requests to HTTPS

# HTTP Strict Transport Security (HSTS) configurations
SECURE_HSTS_SECONDS = 31536000  # Instructs browsers to use HTTPS for a year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Apply HSTS to all subdomains
SECURE_HSTS_PRELOAD = True  # Allow the domain to be part of the browser's HSTS preload list

# Secure cookies to be transmitted only over HTTPS 
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Security headers to protect against various attacks
X_FRAME_OPTIONS = 'DENY'  # Prevents clickjacking by not allowing the site to be framed
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevents MIME-type sniffing by browsers
SECURE_BROWSER_XSS_FILTER = True  # Enables the browser's XSS protection feature

# Documenting the purpose of each security setting
# Comments added directly in settings to explain the security benefits
# Secure Proxy SSL Header
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Ensure that your application only acknowledges requests via HTTPS when behind a proxy.
# SECURE_PROXY_SSL_HEADER is set so Django knows when the request has indeed come over HTTPS.
