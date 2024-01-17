# Generated by Django 4.2.8 on 2024-01-17 09:13

from decimal import Decimal

import djmoney.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0015_alter_siteprofile_integrator"),
    ]

    operations = [
        migrations.AddField(
            model_name="administrativeentity",
            name="min_cfc2_price",
            field=djmoney.models.fields.MoneyField(
                decimal_places=2,
                default=Decimal("4000000.0"),
                help_text="Montant CFC 2 minimal pour les demandes faites à l'entité administrative courante",
                max_digits=12,
                verbose_name="Montant CFC 2 minimal",
            ),
        ),
        migrations.AddField(
            model_name="administrativeentity",
            name="min_cfc2_price_currency",
            field=djmoney.models.fields.CurrencyField(
                choices=[("CHF", "CHF .-"), ("EUR", "EUR €"), ("USD", "USD $")],
                default="CHF",
                editable=False,
                max_length=3,
            ),
        ),
        migrations.AddField(
            model_name="administrativeentity",
            name="services_fees_hourly_rate",
            field=djmoney.models.fields.MoneyField(
                decimal_places=2,
                default=Decimal("0.0"),
                help_text="Tarif horaire des prestations de l'entité administrative",
                max_digits=12,
                verbose_name="Tarif horaire",
            ),
        ),
        migrations.AddField(
            model_name="administrativeentity",
            name="services_fees_hourly_rate_currency",
            field=djmoney.models.fields.CurrencyField(
                choices=[("CHF", "CHF .-"), ("EUR", "EUR €"), ("USD", "USD $")],
                default="CHF",
                editable=False,
                max_length=3,
            ),
        ),
    ]
