import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()

from django.core.management import call_command

import pandas as pd
from csv import DictReader
from models import Products


file_path = 'core/scripts/static/products.csv'

df = pd.read_csv(file_path, delimiter="\t")

for _, row in DictReader(df.iterrows()):
    product = Products(name=row['Наименование'])
    product.save()
