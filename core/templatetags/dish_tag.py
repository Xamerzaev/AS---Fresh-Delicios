from django import template
from ..models import Restaurant, Dish, Product


register = template.Library()


@register.simple_tag()
def get_restaurants():
    """Вывод всех ресторанов"""
    return Restaurant.objects.all()


@register.inclusion_tag('dish_list.html')
def get_last_dishes(count=5):
    dishes = Dish.objects.order_by("id")[:count]
    return {"last_dishes": dishes}


@register.simple_tag()
def get_products():
    """Вывод всех продуктов"""
    return Product.objects.all()