from django.db import models


class Product(models.Model):
    name = models.CharField("Наименование", max_length=16)

    def __str__(self):
        return self.name



class Restaurant(models.Model):
    """Рестораны"""
    name = models.CharField("Ресторан", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ресторан"
        verbose_name_plural = "Рестораны"


class Dish(models.Model):
    """Блюдо"""
    title = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Картинка", upload_to="dishes/")
    products = models.ManyToManyField(Product, verbose_name="продукты")
    url = models.SlugField(max_length=130, unique=True)
    restaurant = models.ForeignKey(
        Restaurant, verbose_name="Ресторан", on_delete=models.SET_NULL, null=True
    )
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"


class RatingStar(models.Model):
    """Звезда рейтинга"""
    value = models.SmallIntegerField("Значение", default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"


class Rating(models.Model):
    """Рейтинг"""
    ip = models.CharField("IP адрес", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="звезда")
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, verbose_name="блюдо")

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class Reviews(models.Model):
    """Отзывы"""
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True
    )
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, verbose_name="блюдо")

    def __str__(self):
        return f"{self.name} - {self.dish}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
