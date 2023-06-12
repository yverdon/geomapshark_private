# Generated by Django 4.2.1 on 2023-06-05 11:55

from django.db import migrations


class Migration(migrations.Migration):
    def set_sent_date_from_simple_history(apps, schema_editor):

        Submission = apps.get_model("submissions", "Submission")
        HistoricalModel = apps.get_model("submissions", "HistoricalSubmission")

        for row in Submission.objects.all():

            last_sent_history = (
                HistoricalModel.objects.filter(id=row.id).exclude(status=1)
                .order_by("history_date")
                .last()
            )

            last_sent_date_value = (
                last_sent_history.history_date
                if last_sent_history is not None
                else None
            )

            row.sent_date = last_sent_date_value
            row.save(update_fields=["sent_date"])

    dependencies = [
        ("submissions", "0018_change_sent_date_into_field"),
    ]

    operations = [
        migrations.RunPython(set_sent_date_from_simple_history),
    ]
