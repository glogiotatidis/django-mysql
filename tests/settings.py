# -*- coding:utf-8 -*-
import os

import django

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DEBUG = False
TEMPLATE_DEBUG = DEBUG

SECRET_KEY = 'THISuISdNOT9A$SECRET9x&ji!vceayg+wwt472!bgs$0!i3k4'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_mysql',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'OPTIONS': {
            'charset': 'utf8mb4',
            # The most forward compatible sql_mode, for 5.7
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES,NO_ZERO_DATE,"
                            "NO_ZERO_IN_DATE,ERROR_FOR_DIVISION_BY_ZERO,"
                            "NO_AUTO_CREATE_USER', innodb_strict_mode=1",
        },
        'TEST': {
            'COLLATION': "utf8mb4_general_ci",
            'CHARSET': "utf8mb4"
        }
    },
    'other': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_mysql2',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'OPTIONS': {
            'charset': 'utf8mb4',
            # The most forward compatible sql_mode, for 5.7
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES,NO_ZERO_DATE,"
                            "NO_ZERO_IN_DATE,ERROR_FOR_DIVISION_BY_ZERO,"
                            "NO_AUTO_CREATE_USER', innodb_strict_mode=1",
        },
        'TEST': {
            'COLLATION': "utf8mb4_general_ci",
            'CHARSET': "utf8mb4"
        }
    },
}

ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_mysql',
    'testapp'
)

if django.VERSION[:2] >= (1, 7):
    INSTALLED_APPS = (
        'django.contrib.admin.apps.AdminConfig',
    ) + INSTALLED_APPS
else:
    INSTALLED_APPS = (
        'django.contrib.admin',
    ) + INSTALLED_APPS

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'urls'
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
STATIC_URL = '/static/'

try:
    from local_settings import *  # noqa
except ImportError:
    pass

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
            ],
        },
    },
]


DJANGO_MYSQL_REWRITE_QUERIES = True
