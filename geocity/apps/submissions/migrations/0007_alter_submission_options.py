# Generated by Django 4.1 on 2022-12-05 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("submissions", "0006_submissionprice_postfinancetransaction_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="submission",
            options={
                "permissions": [
                    ("amend_submission", "Traiter les demandes de permis"),
                    ("validate_submission", "Valider les demandes de permis"),
                    ("classify_submission", "Classer les demandes de permis"),
                    ("edit_submission", "Éditer les demandes de permis"),
                    ("view_private_submission", "Voir les demandes restreintes"),
                    ("can_refund_transactions", "Rembourser une transaction"),
                    ("can_revert_refund_transactions", "Revenir sur un remboursement"),
                ],
                "verbose_name": "2.3 Consultation de la demande",
                "verbose_name_plural": "2.3 Consultation des demandes",
            },
        ),
    ]
