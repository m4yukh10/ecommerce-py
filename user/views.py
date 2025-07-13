from django.shortcuts import render,redirect
from .models import Buyer, Cart
from django.contrib import messages
from seller.models import Products
# Create your views here.

def index(request):
    return render(request, "index2.html")

def register_buyer(request):
    if request.method == "POST":
        name = request.POST['name']
        age = int(request.POST['age'])
        address = request.POST['address']
        
        if age < 18:
            messages.info(request, "you are not an adult yet! can't let ya buy stuff")
        else:
            if Buyer.objects.filter(name=name).exists() == True and Buyer.objects.filter(address=address).exists():
                messages.info(request, "you are already an user. login to get going")
                return redirect("user:login_buyer")
            else:
                Buyer.objects.create(
                    name=name,
                    age=age,
                    address=address
                )
                return redirect("user:login_buyer")      
    return render(request, "registerbuyer.html")

def login_buyer(request):

    if request.method == "POST":

        name = request.POST.get('name')
        address = request.POST.get('address')

        try:
            customer = Buyer.objects.get(name=name, address=address)
            request.session["customer_name"] = customer.name
            return redirect("home")
        except Buyer.DoesNotExist:
            messages.info(request, "go register yoself")
            return redirect("user:register_buyer")

    return render(request, "loginbuyer.html")


from django.contrib import messages
from .models import Cart, Buyer
from seller.models import Products

def buy_product(request):
    if request.method == "POST":
        name = request.POST['product_name']
        product = Products.objects.filter(name=name).first()
        
        buyer_name = request.session.get('customer_name')
        if not buyer_name:
            messages.info(request, "You need to login again")
            return redirect("user:login_buyer")

        buyer = Buyer.objects.get(name=buyer_name)
        cart, created = Cart.objects.get_or_create(buyer=buyer)

        # Add product to cart
        cart.products.add(product)

        # Reduce product quantity
        product.quantity -= 1
        product.save()

        # Count items in cart
        items = cart.products.count()

        messages.success(request, f"{product.name} added to cart!")

        return render(request, "buy.html", {
            "product": product,
            "items": items,
            "user_name": buyer_name
        })

    return redirect("home")
