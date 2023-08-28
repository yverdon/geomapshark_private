# Generated by Django 4.2.1 on 2023-08-03 06:12

import django.db.models.deletion
from django.db import migrations, models

CONTACT_TYPE_OTHER = 0
CONTACT_TYPE_REQUESTOR = 1
CONTACT_TYPE_OWNER = 2
CONTACT_TYPE_COMPANY = 3
CONTACT_TYPE_CLIENT = 4
CONTACT_TYPE_SECURITY = 5
CONTACT_TYPE_ASSOCIATION = 6
CONTACT_TYPE_ENGINEER = 7
CONTACT_TYPE_WORKDIRECTOR = 8
CONTACT_TYPE_CHOICES = (
    (CONTACT_TYPE_OTHER, ("Autres")),  # 0
    (
        CONTACT_TYPE_REQUESTOR,
        ("Requérant (si différent de l'auteur de la demande)"),
    ),  # 1
    (CONTACT_TYPE_OWNER, ("Propriétaire")),  # 2
    (CONTACT_TYPE_COMPANY, ("Entreprise")),  # 3
    (CONTACT_TYPE_CLIENT, ("Maître d'ouvrage")),  # 4
    (CONTACT_TYPE_SECURITY, ("Sécurité")),  # 5
    (CONTACT_TYPE_ASSOCIATION, ("Association")),  # 6
    (CONTACT_TYPE_ENGINEER, ("Architecte/Ingénieur")),  # 7
    (CONTACT_TYPE_WORKDIRECTOR, ("Direction des travaux")),  # 8
)


def create_contact_types(apps, schema_editor):
    """
    Create default contact types based on hardcoded contact types that already exists
    """
    NewContactType = apps.get_model("submissions", "NewContactType")

    contact_types = [
        "Autres",
        "Auteur",
        "Requérant (si différent de l'auteur de la demande)",
        "Propriétaire",
        "Entreprise",
        "Maître d'ouvrage",
        "Sécurité",
        "Association",
        "Architecte/Ingénieur",
        "Direction des travaux",
        "Bénéficiaire",
    ]

    for contact_type in contact_types:
        NewContactType.objects.get_or_create(name=contact_type)


def migrate_contact_type_to_contact_form(apps, schema_editor):
    """
    Migrate all the data in ContactType into ContactForm and using a model for types instead of an enum
    """
    ContactType = apps.get_model("submissions", "ContactType")
    ContactForm = apps.get_model("submissions", "ContactForm")

    contact_types = ContactType.objects.all()
    for contact_type in contact_types:
        ContactForm.objects.create(
            type=contact_type.type,
            is_mandatory=contact_type.is_mandatory,
            form_category=contact_type.form_category,
            integrator=contact_type.integrator,
        )


def migrate_contact_type_based_on_new_model(apps, schema_editor):
    """
    As the data went from a choices field to a foreign key relation, it goes from 1 to 10 instead of 0 to 9, order remains unchanged.
    Incrementing the existing value by 1 is enough to keep the data correct.
    """
    ContactForm = apps.get_model("submissions", "ContactForm")
    HistoricalSubmission = apps.get_model("submissions", "HistoricalSubmission")
    Submission = apps.get_model("submissions", "Submission")
    SubmissionContact = apps.get_model("submissions", "SubmissionContact")
    ContactType = apps.get_model("submissions", "ContactType")

    for contact_form in ContactForm.objects.all():
        if contact_form.type != None:
            type = ContactType.objects.get(
                name=CONTACT_TYPE_CHOICES[contact_form.type][1]
            ).pk
            contact_form.type = type
        else:
            contact_form.type = None
        contact_form.save()

    for historical_submission in HistoricalSubmission.objects.all():
        if historical_submission.creditor_type != None:
            type = ContactType.objects.get(
                name=CONTACT_TYPE_CHOICES[historical_submission.creditor_type][1]
            ).pk
            historical_submission.creditor_type = type
        else:
            historical_submission.creditor_type = None
        historical_submission.save()

    for submission in Submission.objects.all():
        if submission.creditor_type != None:
            type = ContactType.objects.get(
                name=CONTACT_TYPE_CHOICES[submission.creditor_type][1]
            ).pk
            submission.creditor_type = type
        else:
            submission.creditor_type = None
        submission.save()

    for submission_contact in SubmissionContact.objects.all():
        if submission_contact.contact_form != None:
            type = ContactType.objects.get(
                name=CONTACT_TYPE_CHOICES[submission_contact.contact_form][1]
            ).pk
            submission_contact.contact_form = type
        else:
            submission_contact.contact_form = None
        submission_contact.save()


class Migration(migrations.Migration):

    dependencies = [
        ("forms", "0023_category_field_file_types"),
        ("auth", "0012_alter_user_first_name_max_length"),
        ("submissions", "0021_add_contact_type"),
    ]
    atomic = False
    operations = [
        migrations.CreateModel(  # Create ContactType with another name cause already exists
            name="NewContactType",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.RunPython(create_contact_types),  # Add data to NewContactType
        migrations.CreateModel(
            name="ContactForm",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "type",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (7, "Architecte/Ingénieur"),
                            (6, "Association"),
                            (0, "Autres"),
                            (8, "Direction des travaux"),
                            (3, "Entreprise"),
                            (4, "Maître d'ouvrage"),
                            (2, "Propriétaire"),
                            (1, "Requérant (si différent de l'auteur de la demande)"),
                            (5, "Sécurité"),
                            (9, "Bénéficiaire"),
                        ],
                        default=0,
                        verbose_name="type de contact",
                    ),
                ),
                (
                    "is_mandatory",
                    models.BooleanField(default=True, verbose_name="obligatoire"),
                ),
                (
                    "form_category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contact_forms",
                        to="forms.formcategory",
                        verbose_name="type de demande",
                    ),
                ),
                (
                    "integrator",
                    models.ForeignKey(
                        limit_choices_to={
                            "permit_department__is_integrator_admin": True
                        },
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="auth.group",
                        verbose_name="Groupe des administrateurs",
                    ),
                ),
            ],
            options={
                "verbose_name": "1.5 Contact",
                "verbose_name_plural": "1.5 Contacts",
                "unique_together": {("type", "form_category")},
            },
        ),
        migrations.RenameField(
            model_name="submissioncontact",
            old_name="contact_type",
            new_name="contact_form",
        ),
        migrations.RunPython(  # Migrate the data from old ContactType to new ContactForm that replaces it
            migrate_contact_type_to_contact_form
        ),
        migrations.DeleteModel(  # Delete old ContactType that has become ContactForm
            name="ContactType",
        ),
        migrations.RenameModel(  # Rename model as the name is free
            "NewContactType", "ContactType"
        ),
        migrations.AlterField(
            model_name="contactform",
            name="type",
            field=models.IntegerField(
                null=True,
                verbose_name="type de contact",
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubmission",
            name="creditor_type",
            field=models.IntegerField(
                blank=True,
                null=True,
                verbose_name="type de contact",
            ),
        ),
        migrations.AlterField(
            model_name="submission",
            name="creditor_type",
            field=models.IntegerField(
                blank=True,
                null=True,
                verbose_name="type de contact",
            ),
        ),
        migrations.AlterField(
            model_name="submissioncontact",
            name="contact_form",
            field=models.IntegerField(
                verbose_name="type de contact",
            ),
        ),
        migrations.RunPython(migrate_contact_type_based_on_new_model),
        migrations.AlterField(
            model_name="contactform",
            name="type",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="submissions.contacttype",
                verbose_name="type de contact",
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubmission",
            name="creditor_type",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="submissions.contacttype",
                verbose_name="Destinataire de la facture",
            ),
        ),
        migrations.AlterField(
            model_name="submission",
            name="creditor_type",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="submissions.contacttype",
                verbose_name="Destinataire de la facture",
            ),
        ),
        migrations.AlterField(
            model_name="submissioncontact",
            name="contact_form",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="submissions.contacttype",
                verbose_name="type de contact",
            ),
        ),
        migrations.AlterModelOptions(
            name="contacttype",
            options={
                "verbose_name": "1.9 Type de contact",
                "verbose_name_plural": "1.9 Types de contacts",
            },
        ),
        migrations.AddField(
            model_name="contactform",
            name="is_dynamic",
            field=models.BooleanField(
                default=False,
                help_text="Permet à l'utilisateur d'ajouter ce type de contact lors de la saisie, autant de fois que souhaité.",
                verbose_name="Dynamique",
            ),
        ),
        migrations.RenameField(
            model_name="historicalpostfinancetransaction",
            old_name="merchant_reference",
            new_name="transaction_id",
        ),
        migrations.RenameField(
            model_name="postfinancetransaction",
            old_name="merchant_reference",
            new_name="transaction_id",
        ),
        migrations.AlterField(
            model_name="historicalpostfinancetransaction",
            name="transaction_id",
            field=models.CharField(max_length=255, verbose_name="ID transaction"),
        ),
        migrations.AlterField(
            model_name="postfinancetransaction",
            name="transaction_id",
            field=models.CharField(max_length=255, verbose_name="ID transaction"),
        ),
    ]
