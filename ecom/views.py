from django.shortcuts import render, redirect
from seller.models import Products

#views here ->

def home(request):
    customer_name = request.session.get("customer_name", None)
    product = Products.objects.all()
    return render(request, "home.html", {"products": product, "customer_name":customer_name})

    