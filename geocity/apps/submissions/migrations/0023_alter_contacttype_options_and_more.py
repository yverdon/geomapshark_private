# Generated by Django 4.2.1 on 2023-08-07 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("submissions", "0022_contactform_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="contacttype",
            options={
                "verbose_name": "1.9 Type de contact",
                "verbose_name_plural": "1.9 Types de contacts",
            },
        ),
        migrations.AddField(
            model_name="contactform",
            name="is_used_dynamically",
            field=models.BooleanField(
                default=True,
                help_text="Permet à l'utilisateur d'ajouter ce type de contact de manière dynamique lors de la saisie.",
                verbose_name="Peut-être ajouté dynamiquement",
            ),
        ),
    ]
