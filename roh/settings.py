"""
Django settings for roh project.

Generated by 'django-admin startproject' using Django 5.1.7.

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
SECRET_KEY = 'django-insecure-0i@o-tchzup@8x0wle9&c34+%y(0wf6rx5kr&$l@%31%*x!a!*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
     "unfold",  # before django.contrib.admin
    "unfold.contrib.filters",  # optional, if special filters are needed
    "unfold.contrib.forms",  # optional, if special form elements are needed
    "unfold.contrib.inlines",  # optional, if special inlines are needed
    "unfold.contrib.import_export",  # optional, if django-import-export package is used
    "unfold.contrib.guardian",  # optional, if django-guardian package is used
    "unfold.contrib.simple_history",  # optional, if django-simple-history package is used
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
     'drf_yasg',
    'rest_framework',
     'rest_framework.authtoken',
       "corsheaders",
       'nested_admin',
    #apps 
    'inventory',
    'accounts',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
     "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    "https://example.com",
    "https://sub.example.com",
    "http://localhost:3000",
    "http://127.0.0.1:9000",
]

CORS_ALLOW_CREDENTIALS = True
ROOT_URLCONF = 'roh.urls'

SWAGGER_SETTINGS = {
  
    'VALIDATOR_URL': 'http://localhost:8189',
   
}
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'roh.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
}


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
import os

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'accounts.CustomUser'



from django.templatetags.static import static
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

'''     {
            "icon": "people",
            "title": _("Users"),
            "link": reverse_lazy("admin:auth_user_changelist"),
        },'''
UNFOLD = {
    "SITE_TITLE": "Stock Admin",
    "SITE_HEADER": "Stock Management System",
    "SITE_SUBHEADER": "Welcome to Stock Admin",
    "SITE_DROPDOWN": [
        {
            "icon": "diamond",
            "title": _("Stock Dashboard"),
            "link": reverse_lazy("admin:index"),
        },
    ],
    "SITE_URL": "/",
    "SITE_ICON": {
        "light": lambda request: static("icon-light.svg"),
        "dark": lambda request: static("icon-dark.svg"),
    },
    "SITE_LOGO": {
        "light": lambda request: static("logo-light.svg"),
        "dark": lambda request: static("logo-dark.svg"),
    },
    "SITE_SYMBOL": "speed",
    "SITE_FAVICONS": [
        {
            "rel": "icon",
            "sizes": "32x32",
            "type": "image/svg+xml",
            "href": lambda request: static("favicon.svg"),
        },
    ],
    "SHOW_HISTORY": True,
    "SHOW_VIEW_ON_SITE": True,
    "SHOW_BACK_BUTTON": False,
    "SIDEBAR": {
        "show_search": False,
        "show_all_applications": False,
        "navigation": [
            {
                "title": _("Inventory Management"),
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": _("Products"),
                        "icon": "box",
                        "link": reverse_lazy("admin:inventory_product_changelist"),
                    },
                    {
                        "title": _("Categories"),
                        "icon": "folder",
                        "link": reverse_lazy("admin:inventory_category_changelist"),
                    },
                    {
                        "title": _("Brands"),
                        "icon": "tag",
                        "link": reverse_lazy("admin:inventory_brand_changelist"),
                    },
                    {
                        "title": _("Product Attributes"),
                        "icon": "tag",
                        "link": reverse_lazy("admin:inventory_productattribute_changelist"),
                    },
                    {
                        "title": _("Product Types"),
                        "icon": "tag",
                        "link": reverse_lazy("admin:inventory_producttype_changelist"),
                    },
                    {
                        "title": _("Product Inventory"),
                        "icon": "box",
                        "link": reverse_lazy("admin:inventory_productinventory_changelist"),
                    },
                    {
                        "title": _("Media"),
                        "icon": "image",
                        "link": reverse_lazy("admin:inventory_media_changelist"),
                    },
                    {
                        "title": _("Stock"),
                        "icon": "tag",
                        "link": reverse_lazy("admin:inventory_stock_changelist"),
                    },
                    {
                        "title": _("Specifications"),
                        "icon": "list",
                        "link": reverse_lazy("admin:inventory_specification_changelist"),
                    },
                      {
                        "title": _("Specifications group"),
                        "icon": "list",
                        "link": reverse_lazy("admin:inventory_specificationgroup_changelist"),
                    },
                
                
                ],
            },
        ],
    },
}
