# Generated by Django 3.2.13 on 2022-07-14 07:44

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models

import permits.fields
import permits.models


class Migration(migrations.Migration):

    dependencies = [
        ("permits", "0078_create_web_site"),
    ]

    operations = [
        migrations.CreateModel(
            name="PermitSite",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "templatename",
                    models.CharField(
                        blank=True,
                        help_text="Permettant d'afficher la page de login par l'url: https://geocity.ch/?template=vevey",
                        max_length=64,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Seuls les caractères sans accents et les chiffres sont autorisés. Les espaces et autres caractères spéciaux ne sont pas autorisés",
                                regex="^[a-zA-Z0-9_]*$",
                            )
                        ],
                        verbose_name="Identifiant",
                    ),
                ),
                (
                    "application_title",
                    models.CharField(blank=True, max_length=255, verbose_name="Titre"),
                ),
                (
                    "application_subtitle",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Sous-titre"
                    ),
                ),
                (
                    "application_description",
                    models.TextField(
                        blank=True, max_length=2048, verbose_name="Description"
                    ),
                ),
                (
                    "background_image",
                    models.ImageField(
                        blank=True,
                        upload_to="background_images/",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                allowed_extensions=["svg", "png", "jpg", "jpeg"]
                            )
                        ],
                        verbose_name="Image de fond",
                    ),
                ),
                (
                    "background_color",
                    permits.fields.ColorField(
                        default="#FFFFFF",
                        max_length=7,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Ce code de couleur n'est pas valide. Il doit s'agir d'un code couleur HTML, par exemple #000000.",
                                regex="^\\#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$",
                            )
                        ],
                        verbose_name="Couleur unie du fond",
                    ),
                ),
                (
                    "login_background_color",
                    permits.fields.ColorField(
                        default="#FFFFFF",
                        max_length=7,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Ce code de couleur n'est pas valide. Il doit s'agir d'un code couleur HTML, par exemple #000000.",
                                regex="^\\#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$",
                            )
                        ],
                        verbose_name="Couleur unie du fond login",
                    ),
                ),
                (
                    "primary_color",
                    permits.fields.ColorField(
                        default="#008c6f",
                        max_length=7,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Ce code de couleur n'est pas valide. Il doit s'agir d'un code couleur HTML, par exemple #000000.",
                                regex="^\\#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$",
                            )
                        ],
                        verbose_name="Couleur de thème principale",
                    ),
                ),
                (
                    "secondary_color",
                    permits.fields.ColorField(
                        default="#01755d",
                        max_length=7,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Ce code de couleur n'est pas valide. Il doit s'agir d'un code couleur HTML, par exemple #000000.",
                                regex="^\\#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$",
                            )
                        ],
                        verbose_name="Couleur de thème secondaire",
                    ),
                ),
                (
                    "text_color",
                    permits.fields.ColorField(
                        default="#000000",
                        max_length=7,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Ce code de couleur n'est pas valide. Il doit s'agir d'un code couleur HTML, par exemple #000000.",
                                regex="^\\#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$",
                            )
                        ],
                        verbose_name="Couleur du texte",
                    ),
                ),
                (
                    "title_color",
                    permits.fields.ColorField(
                        default="#000000",
                        max_length=7,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Ce code de couleur n'est pas valide. Il doit s'agir d'un code couleur HTML, par exemple #000000.",
                                regex="^\\#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$",
                            )
                        ],
                        verbose_name="Couleur du titre",
                    ),
                ),
                (
                    "table_color",
                    permits.fields.ColorField(
                        default="#212529",
                        max_length=7,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Ce code de couleur n'est pas valide. Il doit s'agir d'un code couleur HTML, par exemple #000000.",
                                regex="^\\#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$",
                            )
                        ],
                        verbose_name="Couleur du texte dans les tableaux",
                    ),
                ),
            ],
            options={
                "verbose_name": "4.1 Configuration de la page de login",
                "verbose_name_plural": "4.1 Configuration des pages de login",
            },
        ),
        migrations.CreateModel(
            name="QgisGeneratedDocument",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "printed_at",
                    models.DateTimeField(null=True, verbose_name="date d'impression"),
                ),
                (
                    "printed_by",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="imprimé par"
                    ),
                ),
                (
                    "printed_file",
                    permits.fields.AdministrativeEntityFileField(
                        blank=True,
                        null=True,
                        storage=permits.fields.PrivateFileSystemStorage(),
                        upload_to=permits.models.printed_permit_request_storage,
                        verbose_name="Permis imprimé",
                    ),
                ),
                (
                    "permit_request",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="qgis_permit",
                        to="permits.permitrequest",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="QgisProject",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "qgis_project_file",
                    permits.fields.AdministrativeEntityFileField(
                        storage=permits.fields.PrivateFileSystemStorage(),
                        upload_to="qgis_templates",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                allowed_extensions=["qgs"]
                            )
                        ],
                        verbose_name="Projet QGIS '*.qgs'",
                    ),
                ),
                (
                    "qgis_print_template_name",
                    models.CharField(
                        max_length=150, verbose_name="Nom du template d'impression QGIS"
                    ),
                ),
                ("description", models.CharField(max_length=150)),
                (
                    "works_object_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="permits.worksobjecttype",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="TemplateCustomization",
        ),
        migrations.AddField(
            model_name="qgisgenerateddocument",
            name="qgis_project",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="qgis_project",
                to="permits.qgisproject",
            ),
        ),
        migrations.AddConstraint(
            model_name="permitsite",
            constraint=models.UniqueConstraint(
                fields=("templatename",), name="unique_templatename"
            ),
        ),
    ]
