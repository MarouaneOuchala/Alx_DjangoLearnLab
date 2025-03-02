# LibraryProject/settings.py

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
DEBUG = False  # Set to False for production

ALLOWED_HOSTS = ['yourdomain.com']

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#212atkrb4)s1biigl0dzo!=6&ma*5kgx1omy!gm+r1_lbllsv'

# SECURITY SETTINGS for HTTPS
SECURE_SSL_REDIRECT = True  # Forces all HTTP traffic to HTTPS
SECURE_HSTS_SECONDS = 31536000  # One year of HSTS
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Apply HSTS to all subdomains
SECURE_HSTS_PRELOAD = True  # Allow HSTS preloading in browsers

# CSRF and session cookies should only be transmitted over HTTPS
CSRF_COOKIE_SECURE = True  # Ensures CSRF cookies are sent over HTTPS
SESSION_COOKIE_SECURE = True  # Ensures session cookies are sent over HTTPS

# Security headers
X_FRAME_OPTIONS = 'DENY'  # Prevents the site from being framed (clickjacking protection)
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevents MIME sniffing
SECURE_BROWSER_XSS_FILTER = True  # Enables browser's XSS filter

# Installed Apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookshelf.apps.BookshelfConfig',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Database configuration (SQLite for development)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
