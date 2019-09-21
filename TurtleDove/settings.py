"""
Django settings for ops_manager_v2 project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import sys
import datetime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
sys.path.insert(0, os.path.join(BASE_DIR, "apps"))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-zwk+-w39l8e96*6muf$v)6f5tzr9yl-4*(sv3ieah4#vnyy)!'

ENCRYPT_KEY = 'passplatairtimes'.encode('utf-8')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]
DOMAIN = '@ykyk.com'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'django_filters',
    'rest_framework.authtoken',
    'channels',
    'gunicorn',
    'menu.apps.MenuConfig',
    'users.apps.UsersConfig',
    'groups.apps.GroupsConfig',
    'resources.apps.ResourcesConfig',
    'products.apps.ProductsConfig',
    'zabbix.apps.ZabbixConfig',
    'opsdocs.apps.OpsdocsConfig',
    'autotask.apps.AutotaskConfig',
    'serverreports.apps.ServerreportsConfig',
    'workorder.apps.WorkorderConfig',
    'projectManager.apps.ProjectmanagerConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'TurtleDove.urls'

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

AUTH_USER_MODEL = "users.User"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'TurtleDove.wsgi.application'
ASGI_APPLICATION = "TurtleDove.routing.application"


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_manager_v4',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '192.168.234.128',
        'PORT': 3306,
        'OPTIONS': {
            'init_command': 'SET default_storage_engine=INNODB;',
        },
    },
    "zabbix": {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': "zabbix",
           'USER': 'root',
           'PASSWORD': "root3306",
           'HOST': "192.168.1.54",
           'PORT': 3306,
           'OPTIONS': {
               'init_command': "SET default_storage_engine=INNODB;"
           }
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

REST_FRAMEWORK = {
    "PAGE_SIZE": 10,
    "DEFAULT_PAGINATION_CLASS": "TurtleDove.paginations.Pagination",
    "DEFAULT_FILTER_BACKENDS": (
        "django_filters.rest_framework.DjangoFilterBackend",
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "TurtleDove.permissions.ModelPermissions",
    ),
}

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(minutes=3600),
    'JWT_AUTH_HEADER_PREFIX': 'JWT',
}

# zabbix
ZABBIX_API = "http://192.168.1.54/zabbix/"
ZABBIX_ADMIN_USER = "Admin"
ZABBIX_ADMIN_PASS = "zabbix"
ZABBIX_DEFAULT_HOSTGROUP = "2"

ZABBIX_INFO = {
        "api": "http://192.168.1.54/zabbix",
        "username": 'admin',
        "password": 'zabbix',
        "login_url": 'http://192.168.1.54/zabbix/index.php',
        "graph_url": 'http://192.168.1.54/zabbix/chart2.php',
        "pie_graph_url": 'http://192.168.1.54/zabbix/chart6.php'
    }
HTML_FILE_PATH = '/tmp/html_files/'
PDF_FILE_PATH = '/tmp/pdf_files/'

# report
REPORT_FILE_PATH = BASE_DIR + '/report_files/'

# Celery
CELERY_BROKER_URL = 'redis://127.0.0.1:6379/11'   # redis作为中间件
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/12'   # 数据结果存储地址

CELERY_TIMEZONE = TIME_ZONE
CELERY_ENABLE_UTC = True
