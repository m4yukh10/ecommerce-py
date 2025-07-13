from django.shortcuts import render, redirect
from .models import Seller, Products
from django.contrib import messages
from django.contrib.auth.models import auth



# Create your views here.

def index(request):
    return render(request, "index.html")


def products(request):
    seller_name = request.session.get('seller_name')
    if seller_name is None:
        return redirect('seller:login')
    
    new = Seller.objects.get(name=seller_name)
    seller_new = new
    new_product = None
    if request.method == "POST":
        seller = seller_new
        productname = request.POST["productname"]
        type = request.POST["type"]
        quantity = int(request.POST["quantity"])
        
        new_product = Products.objects.create(
            seller = seller,
            name=productname,
            type = type,
            quantity=quantity,
            
        )
    existing = Products.objects.filter(seller=seller_new)       
    
    return render(request, "products.html", {"seller":new, "product": new_product, "existing": existing})

def register_seller(request):
    if request.method == "POST":
        name = request.POST["name"]
        pickup = request.POST["pickupAddress"]
        password = request.POST["password"]
        
        if Seller.objects.filter(name=name).exists() == True and Seller.objects.filter(pickupAddress=pickup).exists():
            messages.info(request, 'already exists')
            return redirect('seller:registeruser')
        else:
            seller = Seller.objects.create(name=name, pickupAddress=pickup, password=password)
            return redirect('seller:login')
    return render(request, "registeruser.html")
    

def login(request):
     
    if request.method == "POST":
        name = request.POST["name"]
        pickup = request.POST["pickupAddress"]
        password = request.POST["password"]    
        
        
        if Seller.objects.filter(name=name).exists() == False:
            messages.info(request, "go and register yoself")
            return redirect('seller:registeruser')
        else:
            seller = Seller.objects.get(name=name)
            
            if seller.password == password:
                request.session['seller_name'] = seller.name
                return redirect('seller:products')
                
            else:
                messages.info(request, "invalid credentials!")
                return redirect('seller:registeruser')
                
    return render(request, "login.html")    

       
        