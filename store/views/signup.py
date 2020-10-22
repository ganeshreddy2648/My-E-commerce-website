from django.shortcuts import render, redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password
from django.views import View

class Signup(View):
    def get(self,request):
        return render(request, 'signup.html');
    def post(self,request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password);
        isExists = customer.isExists()
        error_message = None
        if isExists:
            error_message = 'Email already exists'
            print('Email already exists')
            return render(request,'signup.html',{'error':error_message})
        if not error_message:
            customer.password = make_password(customer.password);
            customer.register();
            return redirect('homepage');
