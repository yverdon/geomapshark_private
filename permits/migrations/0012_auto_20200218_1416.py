# Generated by Django 2.2.6 on 2020-02-18 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permits', '0011_auto_20200217_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permitrequestactor',
            name='actor_type',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Autres'), (2, 'Popriétaire'), (3, 'Entreprise'), (4, "Maître d'ouvrage"), (1, "Requérant si différent de l'auteur de la demande"), (5, 'Sécurité'), (6, 'Association')], default=0, verbose_name='type de contact'),
        ),
    ]
