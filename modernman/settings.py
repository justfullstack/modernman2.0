import os
from pathlib import Path
from django.contrib import messages 
from dotenv import load_dotenv




# Load environment variables from .env file
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "fgSaeF%gfgg$fDF4RDDFFGs_fgdrccEtfs%gd"
# SECRET_KEY =  os.getenv("SECRET_KEY", default="")

# for devt only
DEBUG = os.getenv("DEBUG", default=False)

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles', 
    'modernman',
    'shop', 
    'customauth',
    'accounts',
    'checkout',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware', 
    'checkout.middlewares.cartMiddleware',
]

ROOT_URLCONF = 'modernman.urls'

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

WSGI_APPLICATION = 'modernman.wsgi.application'

DB_NAME = os.getenv("DB_NAME", default="")
DB_KEY = os.getenv("DB_KEY", default="")

DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            # "NAME": DB_NAME,
            "NAME": 'modernman',
            "USER": "postgres",
            # "PASSWORD": DB_KEY,
            "PASSWORD": 'sweetpoison',
            "HOST": "localhost",
            "client_encoding": "UTF8"
            }
        }

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images) 
STATIC_URL = 'static/'
# STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "staticfiles")
    ]


STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

# user uploaded media files
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


# messages
MESSAGE_TAGS = {
    messages.ERROR: "danger",

}


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'





# custom user model
AUTH_USER_MODEL = "customauth.CustomUser"



#  email backend
if DEBUG:
    # email
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
else:
    EMAIL_HOST = os.getenv("EMAIL_HOST", default="")
    EMAIL_PORT = os.getenv("EMAIL_PORT", default="")
    EMAIL_HOST_PASSWORD = os.getenv("FCM_NOTIFICATION_APIKEY", default="")
    EMAIL_HOST_USER = os.getenv("EMAIL_HOST_PASSWORD", default="")
    EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS", default=True)
    
    
   
LOGIN_URL = 'login'    
LOGIN_REDIRECT_URL = 'products'
LOGOUT_REDIRECT_URL   = 'login'
    
    
    
# logging
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'verbose': {
#             'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
#             'style': '{',
#         },
#         'simple': {
#             'format': '{levelname} {message}',
#             'style': '{',
#         },
#     },



#     'filters': {
#         'require_debug_true': {
#             '()': 'django.utils.log.RequireDebugTrue',
#         },
#     },

#     'handlers': {
#         'console': {
#             'level': 'INFO',
#             'filters': ['require_debug_true'],
#             'class': 'logging.StreamHandler',
#             'formatter': 'verbose'
#         },
#         'mail_admins': {
#             'level': 'ERROR',
#             'class': 'django.utils.log.AdminEmailHandler',
#             'filters': ['require_debug_true']
#         },
#         'file': {
#             'level': 'ERROR',
#             'class': 'logging.FileHandler',
#             'formatter': 'verbose',
#             'filename': os.path.join(BASE_DIR, 'logs/debug.log'),
#         }
#     },


#     'loggers': {
#         'django': {
#             'handlers': ['console'],
#             'level': 'INFO',
#             'propagate': True,
#         },
#         'django.request': {
#             'handlers': ['console'],
#             'level': 'DEBUG',
#             'propagate': True,

#         },
#         'django.server': {
#             'handlers': ['console'],
#             'level': 'ERROR',
#             'propagate': False,

#         },
#         'modernman_final.custom': {
#             'handlers': ['file'],
#             'formatter': 'verbose',
#             'level': 'ERROR',
#             'filters': ['require_debug_true'],
#             'formatter': 'verbose',
#             'propagate': True,

#         },
#     },
# }

# debug logging   is very verbose as it includes all database queries
DJANGO_LOG_LEVEL = "INFO"    