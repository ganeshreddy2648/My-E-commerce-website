from django.shortcuts import render, redirect
from store.models.product import Product
from store.models.category import Category
from django.views import View


class Index(View):
    def get(self, request):
        products = None
        cart = request.session.get('cart')
        if not cart:
            request.session['cart']={}
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if (categoryID):
            products = Product.get_all_products_by_Categoryid(categoryID)
        else:
            products = Product.get_all_products()
        data = {};
        data['products'] = products
        data['categories'] = categories
        print('you are : ', request.session.get("email"))
        print('email' in request.session)
        return render(request, 'index.html', data)

    def post(self, request):
        product = request.POST.get('product')
        # print(product)
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product]= quantity-1
                else:
                    cart[product] = quantity+1
            else:
                cart[product]=1;
        else:
            cart={}
            cart[product]=1

        print(request.session['cart'])
        request.session['cart']=cart
        return redirect('homepage')
