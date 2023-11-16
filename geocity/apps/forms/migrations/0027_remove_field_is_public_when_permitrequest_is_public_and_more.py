# Generated by Django 4.2.4 on 2023-11-16 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("forms", "0026_alter_form_quick_access_slug"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="field",
            name="is_public_when_permitrequest_is_public",
        ),
        migrations.AddField(
            model_name="field",
            name="api_light",
            field=models.BooleanField(
                default=False,
                help_text="Lorsque cette case est cochée, ce champ est affiché dans la version light de l'api (/rest/RESSOURCE) <b>si la demande est rendue publique par le pilote</b>.<br>\n            Afin de ne pas afficher trop d'informations, le champ est masqué pour améliorer la rapidité de l'API.<br>\n            Pour afficher la version normale de l'api, il faut se rendre sur une seule ressource (/rest/RESSOURCE/:ID).",
                verbose_name="Visible dans l'API light",
            ),
        ),
        migrations.AddField(
            model_name="field",
            name="filter_for_api",
            field=models.BooleanField(
                default=False,
                help_text="Lorsque cette case est cochée, ce champ peut être utilisé pour filtrer <b>si la demande est rendue publique par le pilote</b>.<br>\n            Actuellement ne fonctionne que pour les champs à choix simple ou multiples dans agenda.",
                verbose_name="Filtre pour API",
            ),
        ),
        migrations.AddField(
            model_name="field",
            name="public_if_submission_public",
            field=models.BooleanField(
                default=False,
                help_text="Lorsque cette case est cochée, ce champ est affiché <b>si la demande est rendue publique par le pilote</b>.<br>\n            Actuellement utilisé pour l'application geocalendrier et agenda",
                verbose_name="Information publique",
            ),
        ),
        migrations.AddField(
            model_name="form",
            name="agenda_visible",
            field=models.BooleanField(
                default=False,
                help_text="Lorsque cette case est cochée, les données de ce formulaire sont accessibles dans l'API <b>/rest/agenda/ si la demande est rendue publique par le pilote</b>",
                verbose_name="Visible dans l'agenda",
            ),
        ),
        migrations.AddField(
            model_name="form",
            name="max_submissions_bypass_enabled",
            field=models.BooleanField(
                default=False,
                verbose_name="Autoriser le secrétariat à soumettre des demandes même si le nombre maximal est atteint",
            ),
        ),
        migrations.AlterField(
            model_name="field",
            name="additional_searchtext_for_address_field",
            field=models.CharField(
                blank=True,
                help_text='Ex: "Yverdon-les-Bains" afin de limiter les recherches à Yverdon, <a href="https://api3.Sgeo.admin.ch/services/sdiservices.html#search" target="_blank">Plus d\'informations</a>',
                max_length=255,
                verbose_name="Filtre additionnel pour la recherche d'adresse",
            ),
        ),
    ]
