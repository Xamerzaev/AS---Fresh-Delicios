from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Dish, Rating, RatingStar, Reviews, Restaurant
from ckeditor_uploader.widgets import CKEditorUploadingWidget


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    """Рестораны"""
    list_display = ("id", "name")


class DishAdminForm(forms.ModelForm):
    """Форма с виджетом ckeditor"""
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Dish
        fields = '__all__'


class ReviewInline(admin.TabularInline):
    """Отзывы на странице блюда"""
    model = Reviews
    extra = 1
    readonly_fields = ("name", "email")


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    """Блюда"""
    list_display = ("title", "restaurant", "url", "draft")
    list_filter = ("products", "restaurant")
    search_fields = ("title", "restaurant__name")
    inlines = [ReviewInline]
    save_on_top = True
    save_as = True
    list_editable = ("draft",)
    actions = ["publish", "unpublish"]
    form = DishAdminForm
    readonly_fields = ("get_image",)
    fieldsets = (
        (None, {
            "fields": (("title", "products", "restaurant"),)
        }),
        (None, {
            "fields": ("description", ("poster", "get_image"))
        }),
        ("Options", {
            "fields": (("url", "draft"),)
        }),
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="100" height="110"')

    def unpublish(self, request, queryset):
        """Снять с публикации"""
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request, f"{message_bit}")

    def publish(self, request, queryset):
        """Опубликовать"""
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request, f"{message_bit}")

    publish.short_description = "Опубликовать"
    publish.allowed_permissions = ('change', )

    unpublish.short_description = "Снять с публикации"
    unpublish.allowed_permissions = ('change',)

    get_image.short_description = "Постер"


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """Рейтинг"""
    list_display = ("star", "ip")


admin.site.register(RatingStar)