"""
Django settings for Shicigefu project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import sys
from datetime import timedelta
from corsheaders.defaults import default_headers

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR,"apps"))
sys.path.insert(0, os.path.join(BASE_DIR,"extra_apps"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#z5oi1)9##@&hcq*puee+zmro_6^)p#fh+xhs4d$2sid*4ffc@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# 允许哪些主机访问，*代表全部
ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',#跨域
    'django_filters',#过滤

    #xadmin
    'xadmin',
    'crispy_forms',
    'reversion',

    #ckeditor 富文本编辑器
    'ckeditor',
    'ckeditor_uploader',

    # 第三方登录 migrate(不需要makemigrations)
    'social_django',

    'user.apps.UserConfig',
    'poetry.apps.PoetryConfig',
    'verifycode.apps.VerifycodeConfig',
    'games.apps.GamesConfig',
    'community.apps.CommunityConfig',
    'operation.apps.OperationConfig',
    'notification.apps.NotificationConfig',
]

# 用户模型
AUTH_USER_MODEL = "user.User"

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',# 跨域访问
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


AUTHENTICATION_BACKENDS = (
    # 第三方登录配置格式：social_core.backends.open_id.OpenIdAuth'
    # open_id为social_core中的模块名称（也是社交软件名称），OpenIdAuth为文件中的认证类
    # 'social_core.backends.weibo.WeiboOAuth2',# 微博
    'social_login.weibo.WeiboOAuth2',
    'social_core.backends.qq.QQOAuth2',# qq
    'social_core.backends.weixin.WeixinOAuth2',# 微信
    'django.contrib.auth.backends.ModelBackend',
)


# 跨域设置
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = default_headers + (
        "*",
)

ROOT_URLCONF = 'Shicigefu.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',

                # 第三方登录:上下文处理器
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',

                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Shicigefu.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':  'shicigefu',
        'USER': 'root',
        # 'PASSWORD': 'zou123',
        'PASSWORD': 'bsf123456',
        'HOST': 'localhost',
        'PORT': 3306,
        # 'OPTIONS': { 'init_command': 'SET default_storage_engine=INNODB;' }
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


#rest-framework setting
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES':[
        'rest_framework.renderers.JSONRenderer'
    ],

    #分页设置
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10,

    'DEFAULT_AUTHENTICATION_CLASSES': (
        #Json Web TokenAuthentication
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),

    #ip限速
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '500/minute',
        'user': '1000/minute'
    }
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=10),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
}


#配置邮件信息
EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 465
EMAIL_USE_SSL = True
EMAIL_HOST_USER = 'iscgf@qq.com'
# 密码
EMAIL_HOST_PASSWORD = 'xxxx'
#EMAIL_USE_TLS = True
EMAIL_FROM = 'iscgf@qq.com'


# 第三方登录配置KEY和Secret Key 格式如下：
# SOCIAL_AUTH_{社交软件名}_KEY
# SOCIAL _AUTH_{社交软件名}_SECRET
# 微博
SOCIAL_AUTH_WEIBO_KEY = ''
SOCIAL_AUTH_WEIBO_SECRET = ''
# qq
SOCIAL_AUTH_QQ_KEY = ''
SOCIAL_AUTH_QQ_SECRET = ''
# 微信
SOCIAL_AUTH_WEIXIN_KEY = ''
SOCIAL_AUTH_WEIXIN_SECRET = ''

# 第三方登录成功跳转页面
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/api/v1/'

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# The STATICFILES_DIRS setting should not contain the STATIC_ROOT setting.
STATICFILES_DIRS = []

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# ckeditor settings
CKEDITOR_CONFIGS = {
    'default':{
        'toolbar': 'full',
        'height': 300,
        'width': 900
    }
}
# ckeditor_uploader necessary configuration:文件上次位置
CKEDITOR_UPLOAD_PATH = "uploads"
# 禁用功能：所以上传的文件都会被删除
CKEDITOR_UPLOAD_SLUGIFY_FILENAME = False
# 启用缩略图
CKEDITOR_IMAGE_BACKEND = "pillow"
# 按存储在其中的目录对图像进行分组，并按日期排序
CKEDITOR_BROWSE_SHOW_DIRS = True
# 按年/月/日的目录存储图片
CKEDITOR_RESTRICT_BY_DATE = True
#只允许上传图片
CKEDITOR_ALLOW_NONIMAGE_FILES = False


#诗歌接龙：一回合诗歌数
POEMCOMPLETION_MAX = 8

USERCARD_CONTENT_DEFAULT = "故不登高山，不知天之高也；不临深溪，不知地之厚也；"
