from django.db.models import CharField, ImageField, Model, UniqueConstraint
from PIL import Image

from .nums import CURRENCY_CODES, CURRENCY_DICT, IMAGE_SIZE


class Currency(Model):
    code = CharField(
        "Код валюты",
        max_length=100,
        choices=CURRENCY_CODES,
        unique=True,
    )
    country = CharField(
        "Расшифровка",
        max_length=60,
        null=True,
        blank=True,
        help_text="Будет подобрана автоматически",
    )
    image = ImageField(
        "Изображение купюры",
        upload_to="currency_images/",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Currency"
        verbose_name_plural = "Currencies"
        ordering = ("code",)
        constraints = (
            UniqueConstraint(
                fields=("code", "country"),
                name="Одна валюта на одну страну.",
            ),
        )

    def save(self, *args, **kwargs):
        self.country = CURRENCY_DICT[self.code]
        super().save(*args, **kwargs)
        image = Image.open(self.image.path)
        image.thumbnail(IMAGE_SIZE)
        image.save(self.image.path)
