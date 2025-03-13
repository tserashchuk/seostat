"""
Django settings for seostat project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-h-3jd+he5xec9$0p_--d2v@^3fr5&d5du6aw7i_a^7y3gsfz+!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'topvisor',
    'pagespeed',
    'rest_framework',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_celery_beat',

    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'seostat.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'seostat.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
   'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd9fmgdm0uh014', 
        'USER': 'uev75vgmg517ef',
        'PASSWORD': 'pcf18bd1ca9d06922eeaf4d2a2eea441fb263a75ef140df3ed368abdf575f9bb0',
        'HOST': 'cav8p52l9arddb.cluster-czz5s0kz4scl.eu-west-1.rds.amazonaws.com', 
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}
import os
# REDIS related settings
# REDIS_HOST = 'ec2-52-212-133-20.eu-west-1.compute.amazonaws.com'
# REDIS_PORT = '25020'
# REDIS_PORT = '25020'
# CELERY_BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}
REDIS_URL='rediss://:p7427cde4c1301c0f24f3b41fd538badbc1fda4ecd5c9475649d5e019d9095950@ec2-52-212-133-20.eu-west-1.compute.amazonaws.com:25020'
# for Heroku
CELERY_BROKER_URL = 'rediss://:p7427cde4c1301c0f24f3b41fd538badbc1fda4ecd5c9475649d5e019d9095950@ec2-52-212-133-20.eu-west-1.compute.amazonaws.com:25020'
CELERY_RESULT_BACKEND = 'rediss://:p7427cde4c1301c0f24f3b41fd538badbc1fda4ecd5c9475649d5e019d9095950@ec2-52-212-133-20.eu-west-1.compute.amazonaws.com:25020'
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
CELERY_SEND_EVENTS = True
# Configure Django App for Heroku.
import django_on_heroku
django_on_heroku.settings(locals())