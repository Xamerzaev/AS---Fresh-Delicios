# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

# import django
# django.setup()

# from django.core.management import call_command

import pandas as pd
# from csv import DictReader
from core.models import Product


file_path = 'core/scripts/static/products.csv'

df = pd.read_csv('products.csv', delimiter="\t")

df = df[df['Наименование'].notna()]

for _, row in df.iterrows():
    if row['Наименование']:
        product = Product       (name=row['Наименование'])
        product.save()
