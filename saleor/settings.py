import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

SITE_ID = 1

PROJECT_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))

ROOT_URLCONF = 'saleor.urls'

WSGI_APPLICATION = 'saleor.wsgi.application'

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)
MANAGERS = ADMINS
INTERNAL_IPS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'dev.sqlite',
    }
}

TIME_ZONE = 'Europe/Rome'
LANGUAGE_CODE = 'it'

LANGUAGES = [
    ('it', 'Italiano'),
]

USE_I18N = False
USE_L10N = False
USE_TZ = False

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, 'saleor', 'static'),
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'compressor.finders.CompressorFinder',
]

TEMPLATE_DIRS = [
    os.path.join(PROJECT_ROOT, 'templates'),
    os.path.join(PROJECT_ROOT, 'saleor', 'templates'),
]

CMS_TEMPLATES = (
    # ('content_page.html', 'Content Page'),
    ('product_page.html', 'Product page'),
)


TEMPLATE_LOADERS = [
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.eggs.Loader',
]

# Make this unique, and don't share it with anybody.
SECRET_KEY = 's$au$-tl&u-5m^i5ojzx2qd=lbv=+y5ihr5@or5b(qfaw%f7$n'

MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'cart.middleware.CartMiddleware',
    'saleor.middleware.CheckHTML',
]

DJANGO_CMS_MIDDLEWARES = [
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
]

MIDDLEWARE_CLASSES += DJANGO_CMS_MIDDLEWARES

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

TEMPLATE_CONTEXT_PROCESSORS = [
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    'saleor.context_processors.googe_analytics',
    'saleor.context_processors.canonical_hostname',
    'saleor.context_processors.default_currency',
]

DJANGO_CMS_TEMPLATE_CONTEXT_PROCESSORS = [
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
]

TEMPLATE_CONTEXT_PROCESSORS += DJANGO_CMS_TEMPLATE_CONTEXT_PROCESSORS

INSTALLED_APPS = [
    # External apps that need to go before django's

    # Django modules
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.auth',

    # External apps
    'south',
    'django_prices',
    'mptt',
    'payments',
    'reversion',
    'compressor',

    # Local apps
    'saleor',
    'product',
    'cart',
    'coupon',
    'checkout',
    'registration',
    'payment',
    'delivery',
    'qrcode',
    'userprofile',
    'order',
]


DJANGO_CMS_APPS = [
    'cms',
    'menus',
    'sekizai',
    'filer',
    'easy_thumbnails',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_image',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_video',
    'cms.plugins.link',
    'cms.plugins.text',
]

INSTALLED_APPS += DJANGO_CMS_APPS

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
            '%(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'filters': ['require_debug_true'],
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'saleor': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}

AUTHENTICATION_BACKENDS = (
    'registration.backends.EmailPasswordBackend',
    'registration.backends.ExternalLoginBackend',
    'registration.backends.TrivialBackend',
)

AUTH_USER_MODEL = 'auth.User'

CANONICAL_HOSTNAME = 'localhost:8000'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

LOGIN_URL = '/account/login'

WARN_ABOUT_INVALID_HTML5_OUTPUT = False

SATCHLESS_DEFAULT_CURRENCY = 'EUR'

ACCOUNT_ACTIVATION_DAYS = 3

LOGIN_REDIRECT_URL = "home"

FACEBOOK_APP_ID = "YOUR_FACEBOOK_APP_ID"
FACEBOOK_SECRET = "YOUR_FACEBOOK_APP_SECRET"

GOOGLE_CLIENT_ID = "YOUR_GOOGLE_APP_ID"
GOOGLE_SECRET = "YOUR_GOOGLE_APP_SECRET"

# Adyen settings
# admin / gIsu2ahvCY7k

ADYEN_MERCHANT_ACCOUNT = 'ColpaccioCOM'
ADYEN_MERCHANT_SECRET = 'c(dd)*n*n9ps-kp9+2=p-57%g9ywlgk7#vqfq-0e+%o69iqc2b'
ADYEN_DEFAULT_SKIN = 'zI79cYBf'
ADYEN_ENVIRONMENT = 'test'

PAYMENT_BASE_URL = 'http://%s/' % CANONICAL_HOSTNAME

PAYMENT_MODEL = "payment.Payment"

PAYMENT_VARIANTS = {
    'default': (
        'payments.adyen.AdyenProvider', {
            'skin_code': ADYEN_DEFAULT_SKIN, 'merchant_account': ADYEN_MERCHANT_ACCOUNT
        }
    ),
}

CHECKOUT_PAYMENT_CHOICES = [
    ('default', 'Adyen')
]

import dj_database_url

if os.environ.get('DATABASE_URL'):
    DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')



# Django Compressor Settings
COMPRESS_ENABLED = True

COMPRESS_PRECOMPILERS = (
    ('text/coffeescript', 'coffee --compile --stdio'),
    ('text/less', 'lessc {infile} {outfile}'),
)
