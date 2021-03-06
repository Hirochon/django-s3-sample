import os
try:
    from .local_s import *
except ImportError:
    pass

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'test1',
    'test2',
    'uploadapp',
    'storages',
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

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
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

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript)

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]


# Image files (Image!!)

MEDIA_URL = '/media/'
MEDIAFILES_DIRS = [os.path.join(BASE_DIR, 'media')]

# Logging!!

if DEBUG:
    LOGGING = {
        'version' : 1,                          #バージョンは1に固定
        'disable_existing_loggers' : False,     #既存のログ設定を無効化しない

        #ログフォーマット
        'formatters' : {
            #開発用
            'develop' : {
                'format' : '%(asctime)s [%(levelname)s] %(pathname)s:%(lineno)d %(message)s'
            },
        },
        #ハンドラ
        'handlers' : {
            #コンソール出力用ハンドラ
            'console' : {
                'level' : 'DEBUG',
                'class' : 'logging.StreamHandler',
                'formatter' : 'develop',
            },
        },
        #ロガー
        'loggers' : {
            #自作アプリケーション全般のログを拾うロガー
            '' : {
                'handlers' : ['console'],
                'level' : 'DEBUG',
                'propagate' : False,
            },
            #Django本体が出すログ全般を拾うロガー
            'django' : {
                'handlers' : ['console'],
                'level' : 'INFO',
                'propagate' : False,
            },
            #発行されるSQL文を出力するための設定
            'django.db.backends' : {
                'handlers' : ['console'],
                'level' : 'DEBUG',
                'propagate' : False,
            },
        },
    }