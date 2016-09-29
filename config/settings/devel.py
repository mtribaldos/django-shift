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

