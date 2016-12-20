from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'ecommerce/index.html')

def product(request):
    return render(request, 'ecommerce/product.html')

def admin(request):
    return render(request, 'ecommerce/admin.html')

def orders(request):
    return render(request, 'ecommerce/orders.html')

def products(request):
    return render(request, 'ecommerce/products.html')

def show(request):
    return render(request, 'ecommerce/show.html')
