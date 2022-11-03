# Generated by Django 3.2.13 on 2022-06-29 08:59

import django.core.validators
from django.db import migrations, models

from geocity.apps.accounts.fields import AdministrativeEntityFileField
from geocity.fields import PrivateFileSystemStorage


class Migration(migrations.Migration):

    dependencies = [
        ("reports", "0005_add_report_permission"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="sectionamendproperty",
            options={"verbose_name": "Commentaire·s du secrétariat"},
        ),
        migrations.AlterModelOptions(
            name="sectionvalidation",
            options={"verbose_name": "Commentaire·s des services"},
        ),
        migrations.AlterField(
            model_name="reportlayout",
            name="background",
            field=models.ImageField(
                blank=True,
                help_text='Image d\'arrière plan ("papier à en-tête"). Attention, ces documents ne sont PAS sécurisés',
                null=True,
                upload_to="backgound_paper",
            ),
        ),
        migrations.AlterField(
            model_name="sectionmap",
            name="qgis_print_template_name",
            field=models.CharField(
                blank=True,
                default="a4",
                help_text="Modèles du projet par défaut: a4",
                max_length=30,
            ),
        ),
        migrations.AlterField(
            model_name="sectionmap",
            name="qgis_project_file",
            field=AdministrativeEntityFileField(
                blank=True,
                help_text="Si aucun projet n'est ajouté, le projet par défaut sera utilisé.",
                storage=PrivateFileSystemStorage(),
                upload_to="qgis_templates",
                validators=[
                    django.core.validators.FileExtensionValidator(
                        allowed_extensions=["qgs"]
                    )
                ],
                verbose_name="Projet QGIS '*.qgs'",
            ),
        ),
    ]
