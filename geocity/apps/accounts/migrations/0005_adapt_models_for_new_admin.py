# Generated by Django 3.2.15 on 2022-11-17 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0004_new_admin_models_and_metadata"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="administrativeentity",
            options={
                "permissions": [
                    ("see_private_requests", "Voir les demandes restreintes")
                ],
                "verbose_name": "1.1 Configuration de l'entité administrative (commune, organisation)",
                "verbose_name_plural": "1.1 Configuration des entités administratives (commune, organisation)",
            },
        ),
    ]
