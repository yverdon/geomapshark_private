# Generated by Django 3.1.4 on 2021-05-06 13:40

from django.db import migrations, models
import django.db.models.deletion
import permits.fields
import permits.models


class Migration(migrations.Migration):

    dependencies = [
        ('permits', '0022_add_requires_payment_field_to_works_object_type_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalpermitrequest',
            name='printed_at',
        ),
        migrations.RemoveField(
            model_name='historicalpermitrequest',
            name='printed_by',
        ),
        migrations.RemoveField(
            model_name='historicalpermitrequest',
            name='printed_file',
        ),
        migrations.RemoveField(
            model_name='permitrequest',
            name='printed_at',
        ),
        migrations.RemoveField(
            model_name='permitrequest',
            name='printed_by',
        ),
        migrations.RemoveField(
            model_name='permitrequest',
            name='printed_file',
        ),
        migrations.AddField(
            model_name='permitadministrativeentity',
            name='general_informations',
            field=models.CharField(blank=True, max_length=1024, verbose_name='Informations'),
        ),
        migrations.CreateModel(
            name='QgisProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qgis_project_file', permits.fields.AdministrativeEntityFileField(storage=permits.fields.PrivateFileSystemStorage(), upload_to='qgis_templates', verbose_name="Fichier QGIS '*.qgs'")),
                ('qgis_print_template_name', models.CharField(max_length=150, verbose_name="Nom du template d'impression QGIS")),
                ('qgis_layers', models.CharField(max_length=500, verbose_name="Liste des couches QGIS à afficher séparées par les virgules ','")),
                ('qgis_atlas_coverage_layer', models.CharField(max_length=256, verbose_name="Nom de la couche de couverture de l'atlas ','")),
                ('description', models.CharField(max_length=150)),
                ('works_object_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='permits.worksobjecttype')),
            ],
        ),
        migrations.CreateModel(
            name='QgisGeneratedDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('printed_at', models.DateTimeField(null=True, verbose_name="date d'impression")),
                ('printed_by', models.CharField(blank=True, max_length=255, verbose_name='imprimé par')),
                ('printed_file', permits.fields.AdministrativeEntityFileField(blank=True, null=True, storage=permits.fields.PrivateFileSystemStorage(), upload_to=permits.models.printed_permit_request_storage, verbose_name='Permis imprimé')),
                ('permit_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qgis_permit', to='permits.permitrequest')),
                ('qgis_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qgis_project', to='permits.qgisproject')),
            ],
        ),
    ]
