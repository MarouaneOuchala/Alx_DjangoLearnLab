# LibraryProject/settings.py

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY SETTINGS

DEBUG = False  # Set to False in production

# 1. Secure browser XSS filtering
SECURE_BROWSER_XSS_FILTER = True

# 2. Protect against clickjacking by only allowing your site to be displayed in a frame on the same origin
X_FRAME_OPTIONS = 'DENY'

# 3. Secure content type sniffing
SECURE_CONTENT_TYPE_NOSNIFF = True

# 4. Ensure cookies are only sent over HTTPS
CSRF_COOKIE_SECURE = True  # CSRF cookie is only sent over HTTPS
SESSION_COOKIE_SECURE = True  # Session cookie is only sent over HTTPS

# 5. Prevent HTTP response splitting and ensure secure cookie settings
SECURE_HSTS_SECONDS = 31536000  # Enforce HTTPS for all future requests
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Apply HSTS to subdomains
SECURE_HSTS_PRELOAD = True  # Allows the domain to be included in the HSTS preload list

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookshelf.apps.BookshelfConfig',
    'csp',  # Add the CSP middleware here
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'csp.middleware.CSPMiddleware',  # Enable CSP middleware here
]

# Content Security Policy (CSP)
CSP_DEFAULT_SRC = ("'self'",)
CSP_SCRIPT_SRC = ("'self'", 'https://trusted.cdn.com')
CSP_IMG_SRC = ("'self'", 'https://trusted-images.com')
CSP_STYLE_SRC = ("'self'", 'https://trusted-styles.com')

# Other configurations (DATABASES, etc.) remain unchanged as in the default Django project.
