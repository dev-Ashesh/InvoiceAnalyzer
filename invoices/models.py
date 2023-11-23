from django.db import models


class Invoice(models.Model):
    invoice_number = models.CharField(max_length=255, default="Please fill in.")
    coming_from = models.CharField(max_length=255, default="Please fill in.")
    to = models.CharField(max_length=255, default="Please fill in.")
    date = models.CharField(max_length=255, default="Please fill in.")
    payment_terms = models.CharField(max_length=255, default="Please fill in.")
    due_date = models.CharField(max_length=255, default="Please fill in.")
    po_number = models.CharField(max_length=255, default="Please fill in.")
    balance_due = models.CharField(max_length=255, default="Please fill in.")
    item = models.CharField(max_length=255, default="Please fill in.")
    rate = models.CharField(max_length=255, default="Please fill in.")
    quantity = models.CharField(max_length=255, default="Please fill in.")
    amount = models.CharField(max_length=255, default="Please fill in.")
    subtotal = models.CharField(max_length=255, default="Please fill in.")
    tax = models.CharField(max_length=255, default="Please fill in.")
    total = models.CharField(max_length=255, default="Please fill in.")
    notes = models.CharField(max_length=255, default="Please fill in.")
    terms = models.CharField(max_length=255, default="Please fill in.")
