import datetime

from django.conf import settings
from django.core.management import BaseCommand
from django.utils import timezone
from django.utils.translation import gettext

from geocity.apps.submissions.payments.models import Transaction
from geocity.apps.submissions.payments.postfinance.models import PostFinanceTransaction
from geocity.apps.submissions.payments.services import get_payment_processor


class Command(BaseCommand):
    help = gettext(
        "Update the status of transactions that are pending and not older than %s hours."
        % settings.PAYMENT_PENDING_TRANSACTION_MAX_AGE_MINS
    )

    def handle(self, *args, **options):
        self.stdout.write(
            "Checking status of unpaid transations that are not older than %s minutes..."
            % settings.PAYMENT_PENDING_TRANSACTION_MAX_AGE_MINS
        )

        nb_transactions_confirmed = 0
        nb_transactions_failed = 0
        # Get all unpaid transactions that are not older than the specified time
        transactions_to_update = PostFinanceTransaction.objects.filter(
            status=Transaction.STATUS_UNPAID,
            authorization_timeout_on__gte=timezone.now()
            - datetime.timedelta(
                minutes=settings.PAYMENT_PENDING_TRANSACTION_MAX_AGE_MINS
            ),
        )

        for transaction in transactions_to_update:
            submission = transaction.submission_price.submission
            processor = get_payment_processor(submission.get_form_for_payment())

            if processor.is_transaction_authorized(transaction):
                transaction.confirm_payment()
                nb_transactions_confirmed += 1
            elif processor.is_transaction_failed(transaction):
                transaction.set_failed()
                nb_transactions_failed += 1

        if nb_transactions_confirmed:
            self.stdout.write(
                "Marked %d transactions as confirmed." % nb_transactions_confirmed
            )
        if nb_transactions_failed:
            self.stdout.write(
                "Marked %d transactions as failed." % nb_transactions_failed
            )
        if not nb_transactions_confirmed and not nb_transactions_failed:
            self.stdout.write("No transactions to update.")
