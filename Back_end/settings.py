"""
Django settings for mysite project.


"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#STATICFILES_DIRS = [os.path.join(BASE_DIR, 'mainApp', 'staticfiles'),]
#print (STATICFILES_DIRS)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = False
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'news',
    'mainApp',
    'employment_tests',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    "corsheaders",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'mainApp/react_classification/build'),
            os.path.join(BASE_DIR, 'employment_tests_front_end/build'),
        ],# Переменная DIRS указывает на каталоги в проекте, которые будут содержать шаблоны 
                                                                                #(в основном, мы пользуемся шаблоном index, после npm run build он будет лежать по этому адресу)

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

print(os.path.join(BASE_DIR, 'mainApp/react_classification/build'))

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'investpn_db',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5599'
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

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'mainApp/static')# STATIC_ROOT — указывает на изначально пустую папку, в которую будет собрана вся статика: как project-wide, так и app-specific. Эту папку, в общем случае, должен обслуживать frontend web-сервер (например, nginx).

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'mainApp/react_classification/build/static'),
    os.path.join(BASE_DIR, 'employment_tests_front_end/build/static'),
]

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField' # требования Django, начиная с какой - то версии

# --------------------- Настройка политики CORS ------------------------------
#CSRF_COOKIE_SECURE = False
#CSRF_COOKIE_HTTPONLY = False

#CORS_ORIGIN_ALLOW_ALL = True # Если хотим разрешить все хосты

CORS_ALLOWED_ORIGINS = [    # Разрешаем только стандартный хост среды отладки React
    'http://localhost:3000',
    'http://localhost:8000',
]

#CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_METHODS = [
    "GET",
]

CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
    "Access-Control-Allow-Origin",
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ]
}


# ------------------------ WORKING WITH SERVICES BLOCK ----------------------------

SERVICES_HOSTS = {
    'classifier': 'http://localhost:9090/',
}