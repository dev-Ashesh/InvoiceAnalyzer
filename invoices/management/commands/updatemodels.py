from django.core.management import BaseCommand
from invoices.models import Invoice
import csv

FIELDS = (
'coming_from',
'invoice_number',
'to',
'date',
'payment_terms',
'due_date',
'po_number',
'balance_due',
'item',
'quantity',
'rate',
'amount',
'subtotal',
'tax',
'total',
'notes',
'terms'
)

class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('data.csv') as r:
            reader = csv.reader(r)
            next(reader)
            for row in reader:
                kwargs = {field: val for field, val in zip(FIELDS, row)}
                invoice = Invoice(**kwargs)
                invoice.save()