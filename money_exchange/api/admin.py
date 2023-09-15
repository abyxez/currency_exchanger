from django.contrib.admin import ModelAdmin, register, site
from django.contrib.auth import get_user_model
from django.utils.safestring import mark_safe

from .models import Currency

EMPTY_VALUE_DISPLAY = "-empty-"

site.site_header = "Admin panel"


User = get_user_model()


@register(Currency)
class CurrencyAdmin(ModelAdmin):
    model = Currency
    list_display = (
        "code",
        "country",
        "get_image",
    )
    empty_value_display = EMPTY_VALUE_DISPLAY

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="90" height="40" ')

    get_image.short_description = "Изображение"
