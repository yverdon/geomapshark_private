# Generated by Django 4.1.4 on 2023-02-07 13:31

import django.core.validators
from django.db import migrations

import geocity.apps.reports.fields
import geocity.fields


class Migration(migrations.Migration):

    dependencies = [
        ("reports", "0020_sectionmailing_style_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reportlayout",
            name="background",
            field=geocity.apps.reports.fields.BackgroundFileField(
                blank=True,
                help_text="Image d'arrière plan (PNG ou SVG).",
                null=True,
                storage=geocity.fields.PrivateFileSystemStorage(),
                upload_to="backgound_paper",
                validators=[
                    django.core.validators.FileExtensionValidator(
                        allowed_extensions=["svg", "png"]
                    )
                ],
                verbose_name="Papier à entête",
            ),
        ),
        migrations.AlterField(
            model_name="stylelogo",
            name="logo",
            field=geocity.apps.reports.fields.BackgroundFileField(
                help_text="Image pour logo (PNG ou SVG).",
                storage=geocity.fields.PrivateFileSystemStorage(),
                upload_to="backgound_paper",
                validators=[
                    django.core.validators.FileExtensionValidator(
                        allowed_extensions=["svg", "png"]
                    )
                ],
                verbose_name="Logo",
            ),
        ),
    ]
