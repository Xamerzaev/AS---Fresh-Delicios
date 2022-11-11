import os
import sys
import django

import pandas
import sqlite3

from core.models import Products


proj = os.path.dirname(os.path.abspath('manage.py'))

sys.path.append(proj)

os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'

django.setup()


conn = sqlite3.connect('db.sqlite3')

df = pandas.read_csv('scripts/static/products.csv', sep='encoding')
df.to_sql(Products, conn, if_exists='append', index=False)
