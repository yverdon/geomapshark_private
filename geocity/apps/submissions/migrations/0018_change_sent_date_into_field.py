# Generated by Django 4.2.1 on 2023-06-05 11:55

from django.db import migrations, models


def set_sent_date_from_simple_history(apps, schema_editor):
    Submission = apps.get_model("submissions", "Submission")
    for row in Submission.objects.all():

        last_sent_history = (
            row.history.filter(status=Submission.STATUS_SUBMITTED_FOR_VALIDATION)
            .order_by("history_date")
            .last()
        )
        last_sent_date_value = (
            last_sent_history.history_date if last_sent_history is not None else None
        )

        row.sent_date = last_sent_date_value
        row.save(update_fields=["sent_date"])


class Migration(migrations.Migration):

    dependencies = [
        ("submissions", "0017_alter_submission_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalsubmission",
            name="sent_date",
            field=models.DateTimeField(null=True, verbose_name="date du dernier envoi"),
        ),
        migrations.AddField(
            model_name="submission",
            name="sent_date",
            field=models.DateTimeField(null=True, verbose_name="date du dernier envoi"),
        ),
        migrations.RunPython(set_sent_date_from_simple_history),
    ]
