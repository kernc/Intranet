import os


def next_to_root(*additional_paths):
    return os.path.realpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', *additional_paths))


ADMINS = (
    ('Gasper Zejn', 'zejn@kiberpipa.org'),
    ('Domen Kozar', 'domen@dev.si'),
)
MANAGERS = (
    ('Gasper Zejn', 'zejn@kiberpipa.org'),
)
TIME_ZONE = 'Europe/Ljubljana'
LANGUAGE_CODE = 'sl'
ROOT_URLCONF = 'intranet.urls'

USE_I18N = True
USE_L10N = True

LANGUAGES = (
  ('sl', 'Slovenian'),
  ('en', 'English'),
)

LOCALE_PATHS = (
    next_to_root('locale'),
)

SITE_ID = 1

MEDIA_URL = '/smedia/'
MEDIA_ROOT = next_to_root('media')
STATIC_URL = '/static/'
STATIC_ROOT = next_to_root('static')
ADMIN_MEDIA_PREFIX = STATIC_URL + 'grappelli/'

ALLOWED_HOSTS = [
   "www.kiberpipa.org",
   "new.kiberpipa.org",
]


MIDDLEWARE_CLASSES = (
    'raven.contrib.django.middleware.Sentry404CatchMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    'intranet.middleware.IgnoreBrowserLanguageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'intranet.middleware.FlatPageLocaleURLFallbackMiddleware',
    'honeypot.middleware.HoneypotMiddleware',  # as soon as possible
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.admindocs.middleware.XViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'reversion.middleware.RevisionMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'intranet.org.context_processors.django_settings',
    'intranet.www.context_processors.generate_menu',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.comments',
    'grappelli',  # must be before admin
    'django.contrib.admin',
    'django.contrib.redirects',
    'django.contrib.staticfiles',
    'reversion',
    'feedjack',
    'tagging',
    'south',
    'intranet.org',
    'intranet.www',
    'pipa.video',
    'pipa.ldap',
#    'pipa.ltsp',  # not used anymore
    'pipa.mercenaries',
    'pipa.addressbook',
    'pipa.gallery',
    'honeypot',
    'raven.contrib.django.raven_compat',
    'django_mailman',
    'haystack',  # http://charlesleifer.com/blog/solr-ubuntu-revisited/
    'tinymce',
    'django_gravatar',
    'django_akismet_comments',
    'activelink',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry', 'console'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.handlers.SentryHandler',
            'formatter': 'verbose'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        '()': {
            'level': 'WARNING',
            'handlers': ['sentry'],
        },
        'intranet': {
            'level': 'INFO',
            'handlers': ['console'],
            'propagate': False,
        },
        'pipa': {
            'level': 'INFO',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}


TEMPLATE_DIRS = (
    next_to_root('intranet', 'templates'),
)

FIXTURE_DIRS = (
    next_to_root('fixtures'),
)

# 2 weeks
SESSION_COOKIE_AGE = 2209600

AUTH_PROFILE_MODULE = 'addressbook.PipaProfile'
LOGIN_REDIRECT_URL = '/intranet/'
LOGIN_URL = '/intranet/accounts/login/'
LOGOUT_URL = '/intranet/accounts/logout/'
AUTHENTICATION_BACKENDS = (
    'pipa.ldap.authbackend.LDAPAuthBackend',
    'django.contrib.auth.backends.ModelBackend',
)

PHOTOS_FLICKR_APIKEY = "apikey"
PHOTOS_FLICKR_SECRET = "secret"

LDAP_SERVER = 'ldap://localhost'
SEND_BROKEN_LINK_EMAILS = True
DEFAULT_FROM_EMAIL = 'intranet@kiberpipa.org'
EMAIL_SUBJECT_PREFIX = '[intranet] '

SERVER_EMAIL = 'intranet@kiberpipa.org'
APPEND_SLASH = True

# haystack
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://localhost:8983/solr/intranet/'
    },
}

# south
SOUTH_TESTS_MIGRATE = False

# pipa.photo
PHOTOS_FLICKR_IMAGE_URL_S = 'https://farm%(farm)s.static.flickr.com/%(server)s/%(id)s_%(secret)s_s.jpg'
PHOTOS_FLICKR_SET_IMAGE_URL_N = 'https://farm%(farm)s.static.flickr.com/%(server)s/%(primary)s_%(secret)s_n.jpg'
PHOTOS_FLICKR_IMAGE_URL = 'https://farm%(farm)s.static.flickr.com/%(server)s/%(id)s_%(secret)s.jpg'

# pipa.video
LIVE_STREAM_URL = 'http://live.kiberpipa.org:8100/info/first?password=secret'
PUBLIC_LIVE_STREAM_URL = 'http://live.kiberpipa.org/live.html'

# honeypot
HONEYPOT_FIELD_NAME = "enter_your_email"
HONEYPOT_SKIP_URLS = [u'/intranet/tmp_upload/', u'/intranet/diarys/commit_hook/']

# django-spaminspector
SPAMINSPECTOR_AKISMET_KEY = ""

# tinymce
TINYMCE_JS_URL = STATIC_URL + 'tiny_mce/tiny_mce.js'
TINYMCE_DEFAULT_CONFIG = {
    'theme': 'advanced',
    'theme_advanced_buttons1': 'bold,italic,underline,strikethrough,separator,bullist,numlist,separator,link,unlink,image,separator,undo,redo,removeformat,separator,fullscreen,code',
    'plugins': 'fullscreen',
    'theme_advanced_buttons2': '',
    'theme_advanced_buttons3': '',
    'theme_advanced_toolbar_location': 'top',
}
