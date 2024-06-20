# Generated by Django 4.2.11 on 2024-05-29 15:04

import django_countries.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("submissions", "0030_alter_servicefeetype_fix_price_editable"),
    ]

    operations = [
        migrations.AddField(
            model_name="contact",
            name="country",
            field=django_countries.fields.CountryField(
                max_length=2, null=True, verbose_name="Pays"
            ),
        ),
        migrations.AddField(
            model_name="historicalcontact",
            name="country",
            field=django_countries.fields.CountryField(
                max_length=2, null=True, verbose_name="Pays"
            ),
        ),
    ]
