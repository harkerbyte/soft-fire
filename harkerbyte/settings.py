from pathlib import Path
import os
from decouple import Config, RepositoryEnv
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%d4lk*zmbliye-#1vjv8$v=*y8&yiq1u9d@e=u(k$hl+7a8djx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'games.apps.GamesConfig',
    'storages'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'harkerbyte.urls'

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
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'harkerbyte.wsgi.application'

#READY FOR PRODUCTION? - True / False 
PRODUCTION = True

if PRODUCTION==True:
    #THIS CONDITION USES POSTGRESQL ON DEFAULT
    dbpath = os.path.join(BASE_DIR, '.credentials/db.config')
    configdb = Config(RepositoryEnv(dbpath))
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'postgres',
            'USER':configdb.get('USER'),
            'PASSWORD':configdb.get("PASSWORD"),
            'HOST':configdb.get('HOST'),
            'PORT':configdb.get('PORT')
        }
    }
    
else:
    DATABASES = {
        'default': {
            'ENGINE':'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3'
        }
    }


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


SESSION_COOKIE_SECURE = True

SESSION_COOKIE_AGE = 604800

SESSION_ENGINE = 'django.contrib.sessions.backends.db'


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'harker.share@gmail.com'
EMAIL_HOST_PASSWORD = 'frxr fzjq fufw ykka'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEVELOPER = ['adesolasherifdeen3@gmail.com']


if PRODUCTION==True:
    path = os.path.join(BASE_DIR, '.credentials/.env')
    config = Config(RepositoryEnv(path))
    AWS_ACCESS_KEY_ID=config.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY=config.get('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME=config.get('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_REGION_NAME=config.get('AWS_S3_REGION_NAME')
    AWS_CUSTOM_DOMAIN_NAME=f'https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    AWS_DEFAULT_ACL=None
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl':'max-age=86400'}
    AWS_QUERYSTRING_AUTH = False
    
    #STATIC FILES BUCKET
    
    STATIC_LOCATION = 'static'
    STATIC_URL = f'{AWS_CUSTOM_DOMAIN_NAME}/{STATIC_LOCATION}/'
    STATICFILES_STORAGE = 'harkerbyte.storage_backends.StaticStorage'
    
    #MEDIA FILES BUCKET
    
    MEDIA_LOCATION = 'media'
    MEDIA_URL = f'{AWS_CUSTOM_DOMAIN_NAME}/{MEDIA_LOCATION}/'
    DEFAULT_FILE_STORAGE = 'harkerbyte.storage_backends.MediaStorage'
    
else:
    STATIC_URL = 'static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'Assets')
    
    MEDIA_URL = 'media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
