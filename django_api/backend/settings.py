"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 2.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
# settings.py
from dotenv import load_dotenv
load_dotenv()



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY") #'%-k3e-a3_l9sj!^&sa_9(bf4jm5n_0(lxqbxc&r)n9k-83-u1e'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG")

ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles', 
    'gunicorn',
    # Extend packages
    'rest_framework',  # http://www.django-rest-framework.org/
    'rest_framework.authtoken',
    'corsheaders',  # https://github.com/ottoyiu/django-cors-headers/
    'django_extensions',  # https://github.com/django-extensions/django-extensions
    'api'
    ]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Extend middleware
    'corsheaders.middleware.CorsMiddleware',
]

# corsheaders settings
CORS_ORIGIN_ALLOW_ALL = True


ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['/'],
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

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv("DB_NAME"),
        'USER':os.getenv("DB_USERNAME"),
        'PASSWORD':os.getenv("DB_PASSWORD"),
        'HOST': os.getenv("DB_HOST"),
        'PORT':os.getenv("DB_PORT"),
        'OPTIONS':{
            'init_command':"SET sql_mode='STRICT_TRANS_TABLES'; "
                            # SET GLOBAL max_connections = 151
                            # SET SESSION wait_timeout = 610
                            # SET SESSION interactive_timeout = 610
        }
    }
}

SUB_DIR = os.path.basename(os.path.dirname(__file__))
DATABASE_ROUTERS = [
    '{}.database_router.DatabaseAppsRouter'.format(SUB_DIR)
]
DATABASE_APPS_MAPPING = {
        # example:
        #'app_label':'database_name',
        
}
# 'mysql', 'postgres'需加到INSTALLED_APPS中，它们是通过startapp创建的两个空app


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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

REST_FRAMEWORK_TOKEN_EXPIRE_SECONDS = 3600   #1 hours 3600 seconds
# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'zh-Hant'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
 
STATIC_ROOT = os.path.join(BASE_DIR, 'frontend/dist/static')
 


MEDIA_URL = '/pyapi/media/'
MEDIA_ROOT = '/code/media'

