"""
Django settings for rattler project.

Generated by 'django-admin startproject' using Django 1.11.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# DEBUG = True equals Development-Mode
DEBUG = False

# Charset https://docs.djangoproject.com/en/2.0/ref/settings/#default-charset
DEFAULT_CHARSET = 'utf-8'

# WSGI config
WSGI_APPLICATION = 'rattler.wsgi.application'

# URLs
# https://docs.djangoproject.com/en/2.0/ref/settings/#prepend-www
PREPEND_WWW = False
# https://docs.djangoproject.com/en/2.0/ref/settings/#append-slash
APPEND_SLASH = True
# https://docs.djangoproject.com/en/2.0/ref/settings/#root-urlconf
ROOT_URLCONF = 'rattler.urls'

# Cache Settings https://docs.djangoproject.com/en/2.0/ref/settings/#caches
CACHES = {
    'default': {
        # https://docs.djangoproject.com/en/2.0/topics/cache/#setting-up-the-cache
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        # https://docs.djangoproject.com/en/2.0/ref/settings/#key-prefix
        'KEY_PREFIX': 'rattler',
    },
}

# Databses https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db/database.sqlite'),
        'TEST': {
            'NAME': os.path.join(BASE_DIR, 'db/test.database.sqlite'),
        }
    }
}

# E-Mails
DEFAULT_FROM_EMAIL = 'noreply@rattler.openadaptronik.com'
EMAIL_SUBJECT_PREFIX = '[ Rattler ]'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
SERVER_EMAIL = 'root@rattler.openadaptronik.com'

# File https://docs.djangoproject.com/en/2.0/ref/settings/#file-upload-handlers
FILE_UPLOAD_HANDLERS = [
    'django.core.files.uploadhandler.MemoryFileUploadHandler',
    'django.core.files.uploadhandler.TemporaryFileUploadHandler',
]
DATA_UPLOAD_MAX_MEMORY_SIZE = 3 * 1024 * 1024 # 3MB
FILE_UPLOAD_MAX_MEMORY_SIZE = 3 * 1024 * 1024 # 3 MB
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = 'media/'

# i18n and l10n
USE_I18N = True
USE_L10N = True
USE_TZ = True

# https://docs.djangoproject.com/en/2.0/ref/settings/#language-code
LANGUAGE_CODE = 'de-de'
# https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-TIME_ZONE
TIME_ZONE = 'CET'

# https://docs.djangoproject.com/en/2.0/ref/settings/#first-day-of-week
FIRST_DAY_OF_WEEK = 1
# https://docs.djangoproject.com/en/2.0/ref/settings/#date-format
DATE_FORMAT = 'j F Y'
# https://docs.djangoproject.com/en/2.0/ref/settings/#year-month-format
YEAR_MONTH_FORMAT = 'F Y'
# https://docs.djangoproject.com/en/2.0/ref/settings/#datetime-format
DATETIME_FORMAT = 'j F Y H:i'
# https://docs.djangoproject.com/en/2.0/ref/settings/#month-day-format
MONTH_DAY_FORMAT = 'j F'
# https://docs.djangoproject.com/en/2.0/ref/settings/#short-date-format
SHORT_DATE_FORMAT = 'd.m.Y'
# https://docs.djangoproject.com/en/2.0/ref/settings/#short-date-format
SHORT_DATETIME_FORMAT = 'd.m.Y H:i'
# https://docs.djangoproject.com/en/2.0/ref/settings/#time-format
TIME_FORMAT = 'H:i'


# https://docs.djangoproject.com/en/2.0/ref/settings/#decimal-separator
DECIMAL_SEPARATOR = ','
# https://docs.djangoproject.com/en/2.0/ref/settings/#thousand-separator
THOUSAND_SEPARATOR = '.'
USE_THOUSAND_SEPARATOR = True

# Security Settings
ALLOWED_HOSTS = ['*']
SECRET_KEY = 'dqfc+6=p^h_qo0^j_bs4yb1q%6r%$)=y8)c_q)7s_b$qp4ldx$'

# Installed Apps https://docs.djangoproject.com/en/2.0/ref/settings/#installed-apps
INSTALLED_APPS = [
    'apps.user.apps.UserConfig',
    'apps.register.apps.RegisterConfig',
    'apps.index.apps.IndexConfig',
    'apps.projects.apps.ProjectsConfig',
    'apps.profile.apps.ProfileConfig',
    'apps.process.apps.ProcessConfig',
    'apps.community.apps.CommunityConfig',
    'apps.dashboard.apps.DashboardConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.forms',
]

# Middlewares
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# View Settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'rattler', 'templates')],
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

FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'rattler', 'static'),
]

# Authentication
AUTH_USER_MODEL = 'user.User'
AUTHENTICATION_BACKENDS = ['apps.register.NewModelBackend.NewModelBackend']

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

PASSWORD_HASHERS = ['django.contrib.auth.hashers.BCryptSHA256PasswordHasher']
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 6,
        }
    },
]

# Sessions
SESSION_COOKIE_AGE = 60 * 200 # 15 Minuten = 60*15 = 900 Sekunden TimeOut fuer Sessions
