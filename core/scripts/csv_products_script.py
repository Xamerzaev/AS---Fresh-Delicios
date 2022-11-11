import pandas as pd
from csv import DictReader

from core.models import Products

file_path = 'core/scripts/static/products.csv'

df = pd.read_csv(file_path, delimiter="\t")

for _, row in DictReader(df.iterrows()):
    product = Products(category=row['Категория'],
                       manufacturer=row['Производитель'],
                       name=row['Наименование'],
                       unit=row['Характеристика'],
                       barcode=row['Штрих код'])
    product.save()
