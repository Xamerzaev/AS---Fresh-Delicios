import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

import pandas as pd
from csv import DictReader

from models import Products


def add_data_to_db():
    file_path = 'core/static/products.csv'

    df = pd.read_csv(file_path, delimiter="\t")
    for _, row in DictReader(df.iterrows()):
        product = Products(name=row['Наименование'])
        product.save()


add_data_to_db()
