# Generated by Django 4.2.11 on 2024-05-28 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0019_administrativeentity_agenda_domain"),
    ]

    operations = [
        migrations.AlterField(
            model_name="permitdepartment",
            name="integrator",
            field=models.IntegerField(
                default=0,
                help_text="Identifiant du groupe",
                null=True,
                verbose_name="Groupe des administrateurs",
            ),
        ),
    ]
