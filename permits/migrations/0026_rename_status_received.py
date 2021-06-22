# Generated by Django 3.2.4 on 2021-06-22 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permits', '0025_PermitDepartment_can_set_null_PermitAdministrativeEntity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalpermitrequest',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Brouillon'), (1, 'Envoyée, en attente de traitement'), (4, 'Demande de compléments'), (3, 'En traitement'), (5, 'En validation'), (2, 'Approuvée'), (6, 'Refusée'), (7, 'Réceptionnée')], default=0, verbose_name='état'),
        ),
        migrations.AlterField(
            model_name='permitrequest',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Brouillon'), (1, 'Envoyée, en attente de traitement'), (4, 'Demande de compléments'), (3, 'En traitement'), (5, 'En validation'), (2, 'Approuvée'), (6, 'Refusée'), (7, 'Réceptionnée')], default=0, verbose_name='état'),
        ),
        migrations.AlterField(
            model_name='permitworkflowstatus',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Brouillon'), (1, 'Envoyée, en attente de traitement'), (4, 'Demande de compléments'), (3, 'En traitement'), (5, 'En validation'), (2, 'Approuvée'), (6, 'Refusée'), (7, 'Réceptionnée')], verbose_name='statut'),
        ),
        migrations.AlterField(
            model_name='worksobjecttype',
            name='administrative_entities',
            field=models.ManyToManyField(related_name='works_object_types', to='permits.PermitAdministrativeEntity', verbose_name='entités administratives'),
        ),
    ]
