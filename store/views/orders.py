from django.shortcuts import render, redirect
from django.views import View
from store.models.product import Product
from store.models.orders import Order
from store.models.customer import Customer
from store.models.orders import Order
from store.middlewares.auth import auth_middleware
# from django.utils.decorators import method_decorator

class OrderView(View):
    # @auth_middleware
    # @method_decorator(auth_middleware)
    def get(self, request):
        customer = request.session.get('customer')
        orders = Order.get_orderes_by_customer(customer)
        print(orders)
        return render(request, 'orders.html',{'orders':orders})
