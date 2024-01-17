# Generated by Django 4.2.4 on 2023-09-13 06:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("forms", "0028_form_disable_validation_by_validators"),
        ("submissions", "0023_historicalsubmission_featured_agenda_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalsubmissiongeotime",
            name="field",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="forms.field",
            ),
        ),
        migrations.AddField(
            model_name="historicalsubmissiongeotime",
            name="form",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="forms.form",
            ),
        ),
        migrations.AddField(
            model_name="submissiongeotime",
            name="field",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="geo_time",
                to="forms.field",
            ),
        ),
        migrations.AddField(
            model_name="submissiongeotime",
            name="form",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="geo_time",
                to="forms.form",
            ),
        ),
    ]
