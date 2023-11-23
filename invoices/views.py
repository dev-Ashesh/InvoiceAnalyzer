from django.forms import ValidationError
from django.shortcuts import render, redirect
from .forms import InvoiceForm
from .models import Invoice
import fitz 
import plotly
import plotly.express as px
import pandas as pd
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
FIELDS = (
    'invoice_number',
    'coming_from',
    'to',
    'date',
    'payment_terms',
    'due_date',
    'po_number',
    'balance_due',
    'item',
    'rate',
    'quantity',
    'amount',
    'subtotal',
    'tax',
    'total',
    'notes',
    'terms'
)

INDICES = (2, 0, 4, 6, 8, 10, 12, 14, 19, 21, 20, 22, 24, 26, 28, 30, 32)
@login_required(login_url='login')
def index(request):
    invoices = Invoice.objects.all()
    totals = pd.Series([i[0] for i in Invoice.objects.values_list('total')]).astype('float')
    counts = (totals).value_counts()
    if counts.empty:
        messages.error(request,'Please upload invoice to get started')
        return redirect ('new_invoice')
    else: 
        print("Not empty")
    fig = px.bar(x=counts.index, y=counts.values)
    fig.update_layout(width=500, height=500,xaxis_title="Total Amount on Invoice", yaxis_title="Number of Invoices")
    graph_div = plotly.offline.plot(fig, auto_open=False, output_type='div')

    coming_froms = pd.Series(Invoice.objects.values_list('coming_from', flat=True))
    counts = coming_froms.value_counts()
    fig = px.pie(counts, names=coming_froms, title="Percentage of Invoices stored")
    fig.update_layout(autosize=False, width=500, height=500)
    graph2_div = plotly.offline.plot(fig, auto_open=False, output_type='div')
    context = {'invoices': invoices, 'graph': graph_div, 'graph2': graph2_div}
    return render(request, 'invoices/index.html', context)
    
    

@login_required(login_url='login')
def new_invoice(request):
    if request.method == 'POST':
        # Get file data in chunks
        chunks = request.FILES['file'].chunks()
        # Convert chunks to single bytes object
        encoded = b''.join(chunks)
        with fitz.open('.pdf', encoded) as f:
            text = f.get_page_text(0)        
        # Now extract data from string
        lines = text.splitlines()
        for i, line in enumerate(lines):
            print(str(i).ljust(3), line)
        kwargs = {field: lines[index] for field, index in zip(FIELDS, INDICES)}
        invoice = Invoice(**kwargs)
        invoice.save()
        return redirect('/invoices')

    form = InvoiceForm()
    context = {'form': form}
    return render(request, 'invoices/invoice_form.html', context)


@login_required(login_url='login')
def delete_invoice(request, po_number):
    invoice = Invoice.objects.get(po_number=po_number)
    if request.method == 'POST':
        invoice.delete()
        return redirect('/invoices')
    context = {'invoice': invoice}
    return render(request, 'invoices/delete_invoice.html', context)

@login_required(login_url='login')
def list_invoices(request):
    invoices = Invoice.objects.all()
    p = Paginator(invoices, 10)
    page = request.GET.get('page')
    invoices = p.get_page(page)
    context = {'invoices': invoices}
    return render(request, 'invoices/list_invoices.html', context)

@login_required(login_url='login')
def details(request, po_number):
    invoice = Invoice.objects.get(po_number=po_number)
    total = float(invoice.total) // 5 * 5
    coming_from = invoice.coming_from

    totals = pd.Series([i[0] for i in Invoice.objects.values_list('total')]).astype('float')
    counts = (totals // 5 * 5).value_counts()
    fig = px.bar(x=counts.index, y=counts.values, color=[1 if val == total else 0 for val in counts.index])
    fig.update_layout(width=500, height=500, xaxis_title="Total Amount on Invoice", yaxis_title="Number of Invoices")
    graph_div = plotly.offline.plot(fig, auto_open=False, output_type='div')

    coming_froms = pd.Series(Invoice.objects.values_list('coming_from', flat=True))
    counts = coming_froms.value_counts()
    fig = px.pie(counts, names=coming_froms,title="Percentage of Invoices stored")
#    fig = px.pie(values=counts.values, names=counts.index)
    fig.update_layout(autosize=False, width=500, height=500)
    colors = ['yellow' if i == coming_from else 'white' for i in counts.index]
#    fig.update_traces(marker=dict(colors=colors, line=dict(color='#000000', width=2)))
    fig.update_traces(marker={'colors': colors})
    graph2_div = plotly.offline.plot(fig, auto_open=False, output_type='div')

    context = {'invoice': invoice, 'graph': graph_div, 'graph2': graph2_div}
    return render(request, 'invoices/details.html', context)