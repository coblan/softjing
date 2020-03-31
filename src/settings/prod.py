from .base import *

import pymysql

pymysql.install_as_MySQLdb()


DATABASES = {
     'default': {
        'NAME': 'softjing',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'zhou',
        'PASSWORD': 'zhou570508',
        'HOST': '172.18.215.159', 
        'PORT': '3306', 
        'OPTIONS': {'charset':'utf8mb4'},

      },
} 

ALLOWED_HOSTS=['www.softjing.com','softjing.com']

import os
try:
    with open(os.path.join( os.path.dirname( BASE_DIR ),'git_hash'),'r') as f:
        version = f.read()
        STATIC_URL='https://cdn.jsdelivr.net/gh/coblan@%s/softjing/src/static/'%version
except Exception:
    pass