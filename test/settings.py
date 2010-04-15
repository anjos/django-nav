# Django settings for my personal webpage

DEBUG = True
TEMPLATE_DEBUG = DEBUG
import os

BASEDIR = os.path.dirname(os.path.realpath(__file__)) 
SITE_ID = 1
EMAIL_PORT = 1025
LOGIN_REDIRECT_URL = '/'

DATABASE = os.path.join(BASEDIR, 'db.sql3')

# mail settings for adminstration and management bussiness
ADMINS = (
  ('Site Administrator', 'admin@andreanjos.org'),
)
MANAGERS = (
  ('Andre Anjos', 'andre@andreanjos.org'),
)
DEFAULT_FROM_EMAIL = 'Andre Anjos <andre@andreanjos.org>'

DATABASE_ENGINE = 'sqlite3'    # 'postgresql', 'mysql', 'sqlite3' or 'ado_mssql'.
DATABASE_NAME = DATABASE       # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. All choices can be found here:
# http://www.postgresql.org/docs/current/static/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
TIME_ZONE = 'Europe/Zurich'

# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
# http://blogs.law.harvard.edu/tech/stories/storyReader$15
LANGUAGE_CODE = 'en'
LOCALE_PATHS = [] 

# Valid languages for this website
gettext = lambda s: s
LANGUAGES = (
  ('en', gettext('English')),
  ('pt-br', gettext('Brazilian Portuguese')),
  ('fr', gettext('French')),
  ('es', gettext('Spanish')),
)
DEFAULT_LANGUAGE = 1 

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = BASEDIR 

# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/django/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'awelriaqwpo098bv36256#%$&%asfd409u90-adfg---s+++xx'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

# What we like to have in every page we render, as context
TEMPLATE_CONTEXT_PROCESSORS = (
  'django.core.context_processors.auth', #for users and permissions
  'django.core.context_processors.media', #for MEDIA_URL
  'django.core.context_processors.i18n', #for LANGUAGES 
  'context_processors.full_path', #so we know the current path requested
  'context_processors.current_site', #so we know which site we are in
)

MIDDLEWARE_CLASSES = (
  'django.middleware.common.CommonMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.middleware.locale.LocaleMiddleware',
  'django.middleware.doc.XViewMiddleware',
)

ROOT_URLCONF = 'urls'

# file browser stuff
TEMPLATE_DIRS = (
  # Put strings here, like "/home/html/django_templates".
  # Always use forward slashes, even on Windows.
  BASEDIR,
)

INSTALLED_APPS = (
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.sites',
  'django.contrib.admin',
  'django.contrib.markup',
  'rosetta',
  'order',

  # These are mine
  'nav',
)

