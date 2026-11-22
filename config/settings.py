import os
from pathlib import Path

import dj_database_url
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")


def lista_desde_entorno(nombre):
    return [x.strip() for x in os.getenv(nombre, "").split(",") if x.strip()]


# --- Seguridad y entorno ---
SECRET_KEY = os.environ["SECRET_KEY"]
DEBUG = os.getenv("DEBUG", "False") == "True"
ALLOWED_HOSTS = lista_desde_entorno("ALLOWED_HOSTS")
CSRF_TRUSTED_ORIGINS = lista_desde_entorno("CSRF_TRUSTED_ORIGINS")

# --- Aplicaciones ---
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "apps.usuarios",
    "apps.academico",
    "apps.avisos",
    "apps.principal",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"
ASGI_APPLICATION = "config.asgi.application"

# --- PostgreSQL obligatorio: no hay sustitución por SQLite ---
from django.core.exceptions import ImproperlyConfigured
DATABASE_URL = os.getenv("DATABASE_URL", "")
if not DATABASE_URL.startswith(("postgresql://", "postgres://")):
    raise ImproperlyConfigured("Configurá DATABASE_URL con una conexión PostgreSQL.")
DATABASES = {"default": dj_database_url.parse(
    DATABASE_URL, conn_max_age=60, conn_health_checks=True,
    ssl_require=os.getenv("DATABASE_SSL_REQUIRE", "True").lower() == "true",
)}
DATABASES["default"].setdefault("OPTIONS", {})["connect_timeout"] = 10
DATABASES["default"]["DISABLE_SERVER_SIDE_CURSORS"] = True

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# --- Idioma y zona horaria ---
LANGUAGE_CODE = "es"
TIME_ZONE = "America/Tegucigalpa"
USE_I18N = True
USE_TZ = True

# --- Archivos estáticos y media ---
STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
STORAGES = {
    "default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
    "staticfiles": {"BACKEND": "whitenoise.storage.CompressedStaticFilesStorage"},
}
MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# --- Inicio y cierre de sesión ---
LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "dashboard"
LOGOUT_REDIRECT_URL = "login"

# --- Producción (DEBUG=False) ---
if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
# Clases compartidas definidas en el contrato visual de Paola.
from django.contrib.messages import constants as message_constants
MESSAGE_TAGS = {
    message_constants.SUCCESS: "message--success",
    message_constants.ERROR: "message--error",
    message_constants.WARNING: "message--warning",
    message_constants.INFO: "message--info",
}
