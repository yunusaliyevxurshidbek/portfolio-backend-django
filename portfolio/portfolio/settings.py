from pathlib import Path
import os
from dotenv import load_dotenv
import dj_database_url
from django.core.exceptions import ImproperlyConfigured

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()

SECRET_KEY = 'django-insecure-y#kr_v42^186fccnl*26=n1li52ka)ja+y2^qkl9t%!cul6e32'
DEBUG = True
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')

# apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'base',
    'birthdays',
    'drf_yasg',
    'storages',  
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'portfolio.wsgi.application'

# database:
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ImproperlyConfigured(
        "DATABASE_URL is not set. Define it in your .env for local development "
        "and in the Render dashboard for production."
    )

DATABASES = {
    "default": dj_database_url.parse(
        DATABASE_URL, conn_max_age=600, ssl_require=True
    )
}


AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# internationalization:
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# static_files:
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# cloudflare_settings:
def _env(name: str, default: str | None = None) -> str | None:
    val = os.getenv(name, default)
    return val.strip() if isinstance(val, str) else val

AWS_ACCESS_KEY_ID = _env("R2_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = _env("R2_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = _env("R2_BUCKET_NAME")
AWS_S3_ENDPOINT_URL = _env("R2_ENDPOINT")
R2_ACCOUNT_ID = _env("R2_ACCOUNT_ID")

# endpoint_url:
if AWS_S3_ENDPOINT_URL:
    AWS_S3_ENDPOINT_URL = AWS_S3_ENDPOINT_URL.strip().rstrip("/")
    if not AWS_S3_ENDPOINT_URL.startswith("http"):
        AWS_S3_ENDPOINT_URL = f"https://{AWS_S3_ENDPOINT_URL}"

AWS_S3_REGION_NAME = "auto"
AWS_S3_ADDRESSING_STYLE = "virtual"
AWS_DEFAULT_ACL = None
AWS_QUERYSTRING_AUTH = False
AWS_S3_SIGNATURE_VERSION = "s3v4"

# cloudflare:
AWS_S3_CUSTOM_DOMAIN = (
    f"{AWS_STORAGE_BUCKET_NAME}.{R2_ACCOUNT_ID}.r2.cloudflarestorage.com"
    if AWS_STORAGE_BUCKET_NAME and R2_ACCOUNT_ID
    else None
)

MEDIA_URL = (
    f"https://{AWS_S3_CUSTOM_DOMAIN}/" if AWS_S3_CUSTOM_DOMAIN else 
    f"{AWS_S3_ENDPOINT_URL.rstrip('/')}/{AWS_STORAGE_BUCKET_NAME}/" if AWS_S3_ENDPOINT_URL and AWS_STORAGE_BUCKET_NAME else 
    "/media/"
)
MEDIA_ROOT = BASE_DIR / "media"


STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
        "OPTIONS": {
            "bucket_name": AWS_STORAGE_BUCKET_NAME,
            "custom_domain": AWS_S3_CUSTOM_DOMAIN,
        },
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

AWS_S3_CUSTOM_DOMAIN = (
    f"{AWS_STORAGE_BUCKET_NAME}.{R2_ACCOUNT_ID}.r2.cloudflarestorage.com"
    if AWS_STORAGE_BUCKET_NAME and R2_ACCOUNT_ID
    else None
)
MEDIA_URL = (
    f"https://{AWS_S3_CUSTOM_DOMAIN}/" if AWS_S3_CUSTOM_DOMAIN else 
    f"{AWS_S3_ENDPOINT_URL.rstrip('/')}/{AWS_STORAGE_BUCKET_NAME}/" if AWS_S3_ENDPOINT_URL and AWS_STORAGE_BUCKET_NAME else 
    "/media/"
)
MEDIA_ROOT = BASE_DIR / "media"

if os.getenv("RENDER") or os.getenv("RENDER_EXTERNAL_URL"):
    required = {
        "R2_ACCESS_KEY_ID": AWS_ACCESS_KEY_ID,
        "R2_SECRET_ACCESS_KEY": AWS_SECRET_ACCESS_KEY,
        "R2_BUCKET_NAME": AWS_STORAGE_BUCKET_NAME,
        "R2_ENDPOINT": AWS_S3_ENDPOINT_URL,
    }
    missing = [k for k, v in required.items() if not v]
    if missing:
        raise ImproperlyConfigured(
            "Missing Cloudflare R2 environment variables: " + ", ".join(missing)
        )

