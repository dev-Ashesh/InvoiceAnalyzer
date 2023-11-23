import random
import csv
import datetime
import names

NOTES = "Computer not supplied."
TERMS = "Pay before lesson."
number = 1

rates = {
    "Victoria University": {
        "Python lesson": (15, NOTES, TERMS),
        "R lesson": (17, NOTES, TERMS)
    },
    "UNSW": {
        "Python lesson": (20, NOTES, TERMS),
        "Java lesson": (25, NOTES, TERMS)
    }
}

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

data = {field: [] for field in FIELDS}
for number in range(1, 51):
    coming_from = random.choice(list(rates.keys()))
    invoice_number = number
    to = names.get_full_name()
    min_date = datetime.datetime(2021, 1, 1)
    date = min_date + datetime.timedelta(days=random.randint(0, 365))
    payment_terms = random.randint(1, 60)
    due_date = date + datetime.timedelta(days=payment_terms)
    po_number = date.strftime(f"%d%m%Y-{str(invoice_number).rjust(6, '0')}")
    date = date.strftime("%b %d, %Y")
    due_date = due_date.strftime("%b %d, %Y")
    item = random.choice(list(rates[coming_from].keys()))
    quantity = random.randint(1, 4)
    info = rates[coming_from][item]
    rate = info[0]
    amount = quantity * rate
    subtotal = amount
    tax = 0
    total = subtotal + tax
    balance_due = total
    notes = info[1]
    terms = info[2]
    data2 = [coming_from, invoice_number,
            to,
            date,
            payment_terms,
            due_date,
            po_number,
            balance_due,
            item,
            quantity,
            rate,
            amount,
            subtotal,
            tax,
            total,
            notes,
            terms]
    for d, field in zip(data2, FIELDS):
        data[field].append(d)

with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(data.keys())
    writer.writerows(zip(*data.values()))