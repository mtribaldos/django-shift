# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from os.path import join, normpath
import dj_database_url
from .base import *

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
DATABASES = {
    'default': dj_database_url.config()
}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']

# EDIT HERE ##
SHIFT_GROUP_NAME = 'Guardias'
SHIFT_CARDINALITY = 1000
SHIFT_OFFSET = 1
ANCHOR_DATE = datetime.date(2016, 1, 1)
LOGIN_REDIRECT_URL = "/"

