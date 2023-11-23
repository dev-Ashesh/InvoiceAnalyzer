from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new_invoice', views.new_invoice,name='new_invoice'),
    path('<str:po_number>/details', views.details),
    path('<str:po_number>/delete', views.delete_invoice),
    path('list_invoices', views.list_invoices)
]