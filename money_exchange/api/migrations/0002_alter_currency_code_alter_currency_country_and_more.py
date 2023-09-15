# Generated by Django 4.2.5 on 2023-09-14 14:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="currency",
            name="code",
            field=models.CharField(
                choices=[
                    ("AED", "EmiratiDirham"),
                    ("ARS", "Argentine Peso"),
                    ("AUD", "Australian Dollar"),
                    ("BGN", "Bulgarian Lev"),
                    ("BHD", "Bahraini Dinar"),
                    ("BND", "Bruneian Dollar"),
                    ("BRL", "Brazilian Real"),
                    ("BWP", "Botswana Pula"),
                    ("CAD", "Canadian Dollar"),
                    ("CHF", "Swiss Franc"),
                    ("CLP", "Chilean Peso"),
                    ("CNY", "Chinese Yuan Renminbi"),
                    ("COP", "Colombian Peso"),
                    ("CZK", "Czech Koruna"),
                    ("DKK", "Danish Krone"),
                    ("EUR", "Euro"),
                    ("GBP", "British Pound"),
                    ("HKD", "Hong Kong Dollar"),
                    ("HRK", "Croatian Kuna"),
                    ("HUF", "Hungraian Forint"),
                    ("IDR", "Indonesian Rupiah"),
                    ("ILS", "Israeli Shekel"),
                    ("INR", "Indian Rupee"),
                    ("IRR", "Iranian rial"),
                    ("ISK", "Icelandic Krona"),
                    ("JPY", "Japanese Yen"),
                    ("KWD", "South Korean Won"),
                    ("KRW", "Kuwaiti Dinar"),
                    ("KZT", "Kazakhstani Tenge"),
                    ("LKR", "Sri Lankan Rupee"),
                    ("KYD", "Libyan Dinar"),
                    ("MUR", "Mauritian Rupee"),
                    ("MXN", "Mexican Peso"),
                    ("MYR", "Malaysian Ringgit"),
                    ("NOK", "Norwegian Krone"),
                    ("NPR", "Nepalese Rupee"),
                    ("NZD", "New Zealand Dollar"),
                    ("OMR", "Omani Rial"),
                    ("PHP", "Philippine Peso"),
                    ("PKR", "Pakistani Rupee"),
                    ("PLN", "Polish Zloty"),
                    ("QAR", "Qatari Riyal"),
                    ("RON", "Romanian New Leu"),
                    ("RUB", "Russian Ruble"),
                    ("SAR", "Saudi Arabian Riyal"),
                    ("SEK", "Swedish Krona"),
                    ("SGD", "Singapore Dollar"),
                    ("THB", "Thai Baht"),
                    ("TRY", "Turkish Lira"),
                    ("TTD", "Trinidadian Dollar"),
                    ("TWD", "Taiwan New Dollar"),
                    ("USD", "US Dollar"),
                    ("VEF", "Venezuelan Bolivar"),
                    ("ZAR", "South African Rand"),
                ],
                max_length=100,
                verbose_name="Название валюты",
            ),
        ),
        migrations.AlterField(
            model_name="currency",
            name="country",
            field=models.CharField(max_length=60, verbose_name="Страна валюты"),
        ),
        migrations.AlterField(
            model_name="currency",
            name="image",
            field=models.ImageField(
                blank=True,
                upload_to="currency_images/",
                verbose_name="Изображение купюры",
            ),
        ),
    ]
