# Generated by Django 4.2.4 on 2023-09-15 06:23

import re
import uuid

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("forms", "0026_geom_field_input_type_for_form"),
    ]

    operations = [
        migrations.AlterField(
            model_name="form",
            name="quick_access_slug",
            field=models.TextField(
                blank=True,
                default=uuid.uuid4,
                help_text="Permettant d'accéder directement au formulaire par l'url: https://geocity.ch/?form=URL_COURTE<br>\n            Pour une demande anonyme https://geocity.ch/submissions/anonymous/?form=URL_COURTE",
                unique=True,
                validators=[
                    django.core.validators.RegexValidator(
                        re.compile("^[-a-zA-Z0-9_]+\\Z"),
                        "Enter a valid “slug” consisting of letters, numbers, underscores or hyphens.",
                        "invalid",
                    )
                ],
                verbose_name="URL courte",
            ),
        ),
    ]
