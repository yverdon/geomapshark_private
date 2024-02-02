# Generated by Django 4.2.9 on 2024-01-17 09:13

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("forms", "0029_geom_field_input_type_for_form"),
    ]

    operations = [
        migrations.AlterField(
            model_name="field",
            name="content",
            field=ckeditor.fields.RichTextField(
                help_text="Contenu visible lors de la saisie du formulaire",
                verbose_name="Contenu",
            ),
        ),
    ]
