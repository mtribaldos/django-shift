# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from os.path import join, normpath
import dj_database_url
from .base import *

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
DATABASES['default'] = dj_database_url.config()

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']

