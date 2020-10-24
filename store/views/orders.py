from django.shortcuts import render, redirect
from django.views import View
from store.models.product import Product
from store.models.orders import Order
from store.models.customer import Customer
from store.models.orders import Order


class OrderView(View):
    def get(self, request):
        customer = request.session.get('customer')
        orders = Order.get_orderes_by_customer(customer)
        print(orders)
        return render(request, 'orders.html',{'orders':orders})
