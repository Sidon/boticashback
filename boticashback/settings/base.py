"""
Django settings for boticashback project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import sys
from datetime import timedelta
import yaml


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
SETTINGS_DIR = os.path.dirname(__file__)
PROJECT_ROOT = os.path.split(SETTINGS_DIR)[0]
BASE_DIR = os.path.split(PROJECT_ROOT)[0]

LOG_DIR = os.path.join(BASE_DIR, 'log')
DOC_DIR = os.path.join(BASE_DIR, 'doc')
DATA_DIR = os.path.join(BASE_DIR, 'data')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'gl1ivwd+4xi(y)rh4s5_#jbc1gd&x86#(1h45ltws5xtvi((r#'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'sdn-boticario.herokuapp.com']
DAYS_TO_CASHBACK = None
#
# try:
#     with open('./cashback.yaml', 'r') as f:
#         cashb_settings = yaml.safe_load(f)
#         DAYS_TO_CASHBACK = cashb_settings['days_to_cashback']
# except IOError as e:
#     print("I/O error({0}): {1}".format(e.errno, e.strerror))
#     print("Erro inesperado", sys.exc_info()[0])
#     raise
# except:
#     raise


if not os.path.exists(os.path.join(BASE_DIR, 'logs')):
    os.makedirs(os.path.join(BASE_DIR, 'logs'))
LOG_DIR = os.path.join(BASE_DIR, 'logs')

# Configurações de logs
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s',
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'file_info': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': LOG_DIR + '/info.log',
            'formatter': 'verbose',
            'encoding': 'UTF-8',
        },
        'file_error': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': LOG_DIR + '/error.log',
            'formatter': 'verbose',
            'encoding': 'UTF-8',
        },
        'file_warning': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': LOG_DIR + '/warning.log',
            'formatter': 'verbose',
            'encoding': 'UTF-8',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'apps': {
            'handlers': ['mail_admins', 'console', 'file_info', 'file_error', 'file_warning'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-Party Apps
    'corsheaders',
    'rest_framework',
    'rest_framework_simplejwt',
    'djmoney',
    'django_tables2',
    'django_filters',
    'bootstrap4',
    'django_markup',
    'graphene_django',

    # Local Apps 
    'apps.authcb',
    'apps.reseller',
    'apps.purchase',
    'apps.cashback'
]

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

ROOT_URLCONF = 'boticashback.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'boticashback/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'boticashback.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)


# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# --------------------------
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JSONWebTokenAuthentication',
    ),
}

AUTH_USER_MODEL = 'authcb.User'

try:
    from boticashback.settings.dev import DEV_APPS, DEBUG_TOOLBAR_CONFIG, DEBUG_TOOLBAR_PANELS, DEV_MIDDLEWARE, INTERNAL_IPS

    INSTALLED_APPS += DEV_APPS
    MIDDLEWARE += DEV_MIDDLEWARE
except ImportError:
    pass

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = False

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=480),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
        #'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.BasicAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': None,
}


LOGIN_URL = 'login/'

GRAPHENE = {
    'SCHEMA': 'boticashback.schema.schema',
    'MIDDLEWARE': [
        'graphql_jwt.middleware.JSONWebTokenMiddleware',
    ],
}


AUTHENTICATION_BACKENDS = [
    'graphql_jwt.backends.JSONWebTokenBackend',
    'django.contrib.auth.backends.ModelBackend'
]

GRAPHQL_JWT = {
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_EXPIRATION_DELTA': timedelta(hours=24),
    'JWT_ALLOW_ARGUMENT': True,
}