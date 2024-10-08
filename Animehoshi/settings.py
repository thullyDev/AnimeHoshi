from pathlib import Path
from decouple import config as env_config
import os
import dj_database_url
# import django

# django.setup()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-c*-8b^_eo&qaqt_mgy#+6fb5e$ip%f=10e96s_(_xi)*j(+mx5'

FILE_UPLOAD_MAX_MEMORY_SIZE = 1024 * 1024 * 25  # 25 MB
DATA_UPLOAD_MAX_MEMORY_SIZE = 1024 * 1024 * 25  # 25 MB

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(env_config("DEBUG"))
X_FRAME_OPTIONS = 'ALLOWALL'
# DEBUG = False

# Use secure cookies
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True

ALLOWED_HOSTS = ["*"] if DEBUG else []
CSRF_TRUSTED_ORIGINS = [
    "https://animehoshi2test.onrender.com",
    "https://animehoshitest.onrender.com", #i should probably remove these
]

# Application definition


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'backend',
    # 'backend.apps.BackendConfig',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Animehoshi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / "views"  ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'backend.context_processors.global_context_processors.global_static_data',
            ],
        },
    },
]

WSGI_APPLICATION = 'Animehoshi.wsgi.application'


# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'file': {
#             'level': 'ERROR',
#             'class': 'logging.FileHandler',
#             'filename': 'system.log',
#         },
#         'console': {
#             'class': 'logging.StreamHandler',
#             'level': 'ERROR',
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['file', 'console'],
#             'level': 'ERROR',
#             'propagate': True,
#         },
#     },
# }


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
    # 'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
    # }
# }
DATABASES = {
    'default': {
        'ENGINE': env_config("SQL_ENGINE"),
        'NAME': env_config("SQL_DB"), 
        'USER': env_config("SQL_USER"),
        'PASSWORD': env_config("SQL_PASSWORD"),
        'HOST': env_config("SQL_HOST"), 
        'PORT': env_config("SQL_PORT"),
    }
}
SQL_URL = env_config("SQL_URL")
if SQL_URL != "none": DATABASES["default"] = dj_database_url.parse(SQL_URL) 

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

if DEBUG:
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static'),
   ]
else:
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

INTERNAL_IPS = [
    'localhost',
    '127.0.0.1',
]

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'file': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': BASE_DIR / 'debug.log',  # Specify the full path to the log file
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['file'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#     },
# }