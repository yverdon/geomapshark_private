import os
from datetime import datetime
from distutils.util import strtobool

import diffimg
import pdf2image
from django.conf import settings
from django.contrib.auth.models import Group, User
from django.db import connections, transaction
from django.test import LiveServerTestCase
from django.test.testcases import LiveServerTestCase
from django.utils.timezone import get_default_timezone, make_aware
from freezegun import freeze_time

from geocity.apps.accounts import models as accounts_models
from geocity.apps.accounts.admin import AdministrativeEntityAdmin
from geocity.apps.forms import models as forms_models
from geocity.apps.reports.models import Report
from geocity.apps.submissions import models as submissions_models

UPDATE_EXPECTED_IMAGES = strtobool(os.getenv("TEST_UPDATED_EXPECTED_IMAGES", "false"))


@freeze_time(make_aware(datetime(1985, 7, 4), get_default_timezone()))
class ReportsTestsBase(LiveServerTestCase):
    """Base tests class for testing reports. It runs a live server to allow other containers (QGIS and PDF)
    to communicate with it, provides test fixtures and methods to compare PDFs.

    For this to work, it must run with exposed ports (which means you cannot run the regular web container)"""

    host = "0.0.0.0"
    port = 9000

    # We need to set available_apps for LiveServerTestCase to
    # correctly flush polymorphic models
    available_apps = settings.INSTALLED_APPS

    # Sequences must be reset since IDs appear on the PDF, otherwise rendering
    # will change between successive calls
    reset_sequences = True

    def _reset_sequences(self, db_name):
        # Overriding LiveServerTestCase's implementation because it
        # does not play nice with polymorphic... (throws
        # psycopg2.ProgrammingError: can't adapt type '__proxy__')
        # Here we manually reset the sequences for all tables
        conn = connections[db_name]
        with transaction.atomic(using=db_name):
            with conn.cursor() as cursor:
                # Get tablename, pk_column for all tables in public
                cursor.execute(
                    """
                    select
                        kcu.table_name,
                        kcu.column_name as pk_column
                    from
                        information_schema.table_constraints tco
                    join information_schema.key_column_usage kcu on
                        kcu.constraint_name = tco.constraint_name
                        and kcu.constraint_schema = tco.constraint_schema
                        and kcu.constraint_name = tco.constraint_name
                    where
                        tco.constraint_type = 'PRIMARY KEY'
                        and kcu.table_schema = 'public'
                    """
                )
                for table_name, pk_name in cursor.fetchall():
                    # hacky used to skip knox digest pk which is a varchar
                    if not pk_name.endswith("id"):
                        continue
                    query = f"SELECT setval(pg_get_serial_sequence('{table_name}', '{pk_name}'), coalesce(max({pk_name}),0) + 1, false) FROM {table_name}"
                    cursor.execute(query)

    # This seems not necessary, wrote it because at some point I had strange issues
    # where fixtures did not seem to properly delete... Keeping it in case it
    # def _fixture_teardown(self):
    #     # Overriding LiveServerTestCase's implementation because it
    #     # does not play nice with polymorphic...
    #     # We manually call TRUNCATE on all tables.
    #     for db_name in self._databases_names(include_mirrors=False):
    #         conn = connections[db_name]
    #         with transaction.atomic(using=db_name):
    #             with conn.cursor() as cursor:
    #                 cursor.execute(
    #                     "SELECT table_name FROM information_schema.tables WHERE table_type = 'BASE TABLE' AND table_schema = 'public'"
    #                 )
    #                 tables = [row[0] for row in cursor.fetchall()]
    #                 tables_list = ','.join(tables)
    #                 query = f"TRUNCATE {tables_list}"
    #                 cursor.execute(query)

    def setUp(self):

        # Create the user
        user = User.objects.create(
            username="user",
            is_superuser=True,
        )
        group = Group.objects.create(name="group")
        user.groups.set([group])

        # Create the admin entity
        admin_entity = accounts_models.AdministrativeEntity.objects.create(
            name="entity",
            group_order=1,
            integrator=group,
            geom="SRID=2056;MultiPolygon (((2538512 1181638, 2538447 1180620, 2539787 1180606, 2539784 1181553, 2538512 1181638)))",
        )
        dept = accounts_models.PermitDepartment.objects.create(
            administrative_entity=admin_entity,
            group=group,
            is_validator=True,
            is_integrator_admin=True,
            is_backoffice=True,
            is_default_validator=True,
        )
        author = accounts_models.UserProfile.objects.create(
            user=user,
            company_name="company_name",
            vat_number="vat_number",
            address="address",
            zipcode=1000,
            city="city",
            phone_first="phone_first",
            phone_second="phone_second",
        )

        # Create and configure the work object type
        category = forms_models.FormCategory.objects.create(name="type")
        form = forms_models.Form.objects.create(
            category=category,
            is_public=True,
            document_enabled=True,
        )
        field = submissions_models.SubmissionAmendField.objects.create(
            name="field",
        )
        field.forms.set([form])
        status = submissions_models.SubmissionWorkflowStatus.objects.create(
            status=submissions_models.Submission.STATUS_PROCESSING,
            administrative_entity=admin_entity,
        )

        # Create the submission
        submission = submissions_models.Submission.objects.create(
            administrative_entity=admin_entity,
            author=author.user,
            status=submissions_models.Submission.STATUS_PROCESSING,
        )
        selected_form = submissions_models.SelectedForm.objects.create(
            submission=submission,
            form=form,
        )

        submissions_models.SubmissionGeoTime.objects.create(
            submission=submission,
            geom="SRID=2056;GEOMETRYCOLLECTION (MultiPolygon (((2539069 1181160, 2539052 1181120, 2539099 1181110, 2539118 1181147, 2539069 1181160))))",
        )
        submissions_models.SubmissionAmendFieldValue.objects.create(
            field=field,
            form=selected_form,
            value="myvalue",
        )

        # Create the document type
        parent_doc_type = submissions_models.ComplementaryDocumentType.objects.create(
            name="parent",
            form=form,
        )
        doc_type = submissions_models.ComplementaryDocumentType.objects.create(
            name="child",
            parent=parent_doc_type,
        )

        AdministrativeEntityAdmin.create_default_report(
            AdministrativeEntityAdmin, None, admin_entity.pk
        )

        # Assign the report (normally, one should have been created automatically)
        report = Report.objects.filter(integrator=group).first()
        report.document_types.set([doc_type])

        # Make fixtures available to testcase
        self.submission = submission
        self.form = form
        self.report = report
        self.doc_type = doc_type
        self.user = user
        self.dept = dept

    @property
    def data_dir(self):
        """Where to find/store expected/generated images"""
        return os.path.join(os.path.dirname(__file__), "data", self._testMethodName)

    def assert_pdf_is_as_expected(self, pdf_bytes: bytes, pdf_name="page"):

        # Compare the generated PDF against the expected images
        if UPDATE_EXPECTED_IMAGES:
            os.makedirs(self.data_dir, exist_ok=True)
        differences = []
        pages = pdf2image.convert_from_bytes(pdf_bytes, 200)
        for i, page in enumerate(pages):
            page_name = f"{pdf_name}-{i:0>3}"
            expected_path = os.path.join(self.data_dir, f"{page_name}.expected.png")
            generated_path = os.path.join(self.data_dir, f"{page_name}.generated.png")
            diff_path = os.path.join(self.data_dir, f"{page_name}.result.png")

            if UPDATE_EXPECTED_IMAGES:
                page.save(expected_path, "PNG")
            page.save(generated_path, "PNG")

            ratio = diffimg.diff(
                generated_path,
                expected_path,
                diff_img_file=diff_path,
            )

            # For now we tolerate very small difference (0.01%) which seem to happen for unknown reason,
            # maybe difference in antialiasing or whatnot. At some point we may need to implement
            # support for masks (areas that are not compared) to allow negligible rendering differences,
            # e.g. for QGIS updates.
            if ratio > 0.0001:
                differences.append(f"{page_name}: {ratio*100}%")

        if differences:
            differences_txt = "\n".join(differences)
            raise AssertionError(
                f"The following rendering differences were detected:\n{differences_txt}"
            )
