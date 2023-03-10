# Generated by Django 4.1.7 on 2023-03-10 13:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("forms", "0019_add_related_name_for_fk"),
        ("accounts", "0012_add_fields_for_new_map_widget"),
    ]

    operations = [
        migrations.AlterField(
            model_name="administrativeentity",
            name="map_widget_configuration",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="map_widget_configuration_administrative_entity",
                to="forms.mapwidgetconfiguration",
                verbose_name="Configuration de la carte avancée",
            ),
        ),
    ]
