from pathlib import Path
import os
from decouple import config
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# -------------------------------------------------------------------
# 1. БЕЗОПАСНОСТЬ И РЕЖИМЫ (DEBUG, SECRET_KEY)
# -------------------------------------------------------------------

# SECRET_KEY: Берется из переменной окружения (файла .env или настроек Render)
SECRET_KEY = config('SECRET_KEY', default='django-insecure-g_b$dppcebc+ja!+5oi5(5ebjcqnrhb!_&v618fss8%zux2g$y')

# DEBUG: Берется из переменной окружения. Локально = True, на Render = False
DEBUG = config('DEBUG', default=True, cast=bool)

# ALLOWED_HOSTS: Должен разрешать домен Render
ALLOWED_HOSTS = ['*']
if not DEBUG:
    # Разрешает доступ со всех субдоменов Render.com в продакшене
    ALLOWED_HOSTS = ['.onrender.com']


# -------------------------------------------------------------------
# 2. Application definition (ПРИЛОЖЕНИЯ)
# -------------------------------------------------------------------

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # 🌟 Добавляем Cloudinary для медиафайлов
    'cloudinary',
    'cloudinary_storage',
    
    # Ваши приложения
    'shop.apps.ShopConfig',
    'cart.apps.CartConfig',
    'orders.apps.OrdersConfig',
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

ROOT_URLCONF = 'amazon_clone.urls'

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

WSGI_APPLICATION = 'amazon_clone.wsgi.application'


# -------------------------------------------------------------------
# 3. Database (PostgreSQL / SQLite)
# -------------------------------------------------------------------
# Автоматически переключается на PostgreSQL, если задана DATABASE_URL (на Render).
# Локально использует SQLite.

DATABASES = {
    'default': dj_database_url.config(
        default=f'sqlite:///{os.path.join(BASE_DIR, "db.sqlite3")}',
        conn_max_age=600
    )
}


# Password validation (настройки по умолчанию)
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
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# -------------------------------------------------------------------
# 4. Static Files (CSS, JS)
# -------------------------------------------------------------------

STATIC_URL = 'static/'
# STATIC_ROOT нужен для Render, чтобы собрать всю статику для продакшена
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# -------------------------------------------------------------------
# 5. Media Files (Картинки товаров) - CLOUDINARY
# -------------------------------------------------------------------

# Указываем, что медиафайлы должны храниться через Cloudinary
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Настройки подключения к Cloudinary (Берутся из переменных окружения Render)
CLOUDINARY_CLOUD_NAME = config('CLOUDINARY_CLOUD_NAME', default='')
CLOUDINARY_API_KEY = config('CLOUDINARY_API_KEY', default='')
CLOUDINARY_API_SECRET = config('CLOUDINARY_API_SECRET', default='')

# MEDIA_URL и MEDIA_ROOT можно оставить как запасной вариант для локального dev, 
# но Cloudinary будет использовать свои URL в продакшене.
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


CART_SESSION_ID = 'cart' # Ключ, по которому корзина хранится в сессии


# -------------------------------------------------------------------
# 6. АВТОРИЗАЦИЯ И КОМАНДЫ ЗАПУСКА
# -------------------------------------------------------------------

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Команда для создания администратора после миграции (только для продакшена)
# Эта переменная будет использоваться в Procfile для выполнения команды release:
if not DEBUG:
    ADMIN_CREATION_COMMAND = f"python manage.py shell < {os.path.join(BASE_DIR, 'create_admin.py')}"
    POST_MIGRATE_COMMANDS = [ADMIN_CREATION_COMMAND]
else:
    POST_MIGRATE_COMMANDS = []
