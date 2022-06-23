# Generated by Django 3.2.13 on 2022-06-23 17:19

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("reports", "0004_sectionstatus"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sectionparagraph",
            name="content",
            field=ckeditor.fields.RichTextField(
                help_text='Il est possible d\'inclure des variables et de la logique avec la <a href="https://jinja.palletsprojects.com/en/3.1.x/templates/">syntaxe Jinja</a>. Les variables de la demande sont accessible dans `{{request_data}}` et clles du work object type dans `{{wot_data}}`.'
            ),
        ),
    ]
