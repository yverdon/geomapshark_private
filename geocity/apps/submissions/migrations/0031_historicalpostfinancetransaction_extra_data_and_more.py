# Generated by Django 4.2.11 on 2024-06-06 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("submissions", "0030_alter_servicefeetype_fix_price_editable"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalpostfinancetransaction",
            name="extra_data",
            field=models.JSONField(
                default=dict, verbose_name="Données supplémentaires"
            ),
        ),
        migrations.AddField(
            model_name="postfinancetransaction",
            name="extra_data",
            field=models.JSONField(
                default=dict, verbose_name="Données supplémentaires"
            ),
        ),
    ]
