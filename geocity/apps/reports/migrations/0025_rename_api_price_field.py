# Generated by Django 4.1.7 on 2023-04-21 15:39

from django.db import migrations


def rename_api_price_field(apps, schema_editor):
    # Rename `submission_submission_price` to `submission_price` in reports

    SectionParagraph = apps.get_model("reports", "SectionParagraph")

    paragraphs = SectionParagraph.objects.filter(
        content__contains="submission_submission_price"
    )
    for paragraph in paragraphs:
        paragraph.content = paragraph.content.replace(
            "submission_submission_price", "submission_price"
        )
        paragraph.save()


class Migration(migrations.Migration):

    dependencies = [
        ("reports", "0024_sectionamendproperty_show_form_name_and_more"),
    ]

    operations = [
        migrations.RunPython(rename_api_price_field),
    ]
