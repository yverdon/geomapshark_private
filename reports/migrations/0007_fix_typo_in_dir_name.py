# Generated by Django 3.2.13 on 2022-06-29 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reports", "0006_set_background_file_public_and_switch_blocks_names"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reportlayout",
            name="background",
            field=models.ImageField(
                blank=True,
                help_text='Image d\'arrière plan ("papier à en-tête"). Attention, ces documents ne sont PAS sécurisés',
                null=True,
                upload_to="background_paper",
            ),
        ),
    ]
