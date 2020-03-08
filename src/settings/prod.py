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