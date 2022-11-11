from django.db import models


class Products(models.Model):
    category = models.CharField("Категория", max_length=25)
    manufacturer = models.CharField("Производитель", max_length=40)
    name = models.CharField("Наименование", max_length=16)
    unit = models.IntegerField("Единица измерения")
    barcode = models.IntegerField("Штрих-код")
