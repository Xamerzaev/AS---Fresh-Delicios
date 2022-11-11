import pandas as pd
from csv import DictReader
from models import Products
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

file_path = 'core/scripts/static/products.csv'

df = pd.read_csv(file_path, delimiter="\t")
if __name__ == '__main__':
    for _, row in DictReader(df.iterrows()):
        product = Products(name=row['Наименование'])
        product.save()
