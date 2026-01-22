from django.shortcuts import render
from . models import Customers, Order

def Order_list(request):
    maua = Order.object.all()
    return render (request, 'list.html', {'maua': maua})

def customer_list(request):
    customer = Customers.object.all()
    return render(request, 'list.html', {'customer': customer})