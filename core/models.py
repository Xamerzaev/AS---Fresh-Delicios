from django.db import models


class Products(models.Model):
    name = models.CharField("Наименование", max_length=16)

    def __str__(self):
        return self.name
