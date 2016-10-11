# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from os.path import join, normpath
from .base import *


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# EDIT HERE ##
SHIFT_GROUP_NAME = 'Guardias'
SHIFT_CARDINALITY = 1000
SHIFT_USERS = ['mtribaldos', 'jorgecremades', 'mortega', 'dgalera', 'pacoma']
ANCHOR_DATE = datetime.date(2016, 1, 1)
LOGIN_REDIRECT_URL = "/"

