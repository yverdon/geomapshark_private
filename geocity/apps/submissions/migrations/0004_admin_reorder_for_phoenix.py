# Generated by Django 3.2.15 on 2022-11-10 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0003_migrate_permits_data'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='complementarydocumenttype',
            options={'verbose_name': '2.2 Type de document', 'verbose_name_plural': '2.2 Types de document'},
        ),
        migrations.AlterModelOptions(
            name='contacttype',
            options={'verbose_name': '1.5 Contact', 'verbose_name_plural': '1.5 Contacts'},
        ),
    ]
