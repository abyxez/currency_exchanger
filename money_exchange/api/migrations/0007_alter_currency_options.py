# Generated by Django 4.2.5 on 2023-09-14 15:18

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0006_alter_currency_country"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="currency",
            options={
                "ordering": ("code",),
                "verbose_name": "Валюта",
                "verbose_name_plural": "Перечень валют",
            },
        ),
    ]
