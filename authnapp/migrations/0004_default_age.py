# Generated by Django 2.2.18 on 2021-03-11 14:51

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ("authnapp", "0003_default_age"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shopuser",
            name="activation_key_expires",
            field=models.DateTimeField(
                default=datetime.datetime(2021, 3, 13, 14, 51, 42, 83142, tzinfo=utc), verbose_name="актуальность ключа"
            ),
        ),
    ]
