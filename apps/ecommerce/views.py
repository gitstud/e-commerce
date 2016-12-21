from django.shortcuts import render, redirect, reverse
from .models import Products
# Create your views here.
def index(request):
    if 'cart' not in request.session:
        request.session['cart'] = {}
        items = Products.objects.all()
        for item in items:
            pk = str(item.id)
            quantity = {'quantity':2}
            request.session['cart'][pk]=quantity

    print request.session['cart']
    return render(request, 'ecommerce/index.html')

def product(request):
    return render(request, 'ecommerce/product.html')

def admin(request):
    return render(request, 'ecommerce/admin.html')

def orders(request):
    return render(request, 'ecommerce/orders.html')

def products(request):
    products = Products.objects.all().filter(ongoing=True)
    context = {
            'products': products
            }
    return render(request, 'ecommerce/products.html', context)

def show(request):
    return render(request, 'ecommerce/show.html')

def test(request):
    return render(request, 'ecommerce/test.html')

def add_product(request):
    product = Products.objects.add_product(form_data=request.POST)
    return redirect(reverse('products'))

def delete(request, id):
    product = Products.objects.get(id=id)
    product.ongoing = False
    product.save()
    return redirect(reverse('products'))

def edit(request, id):
    edit_product = Products.objects.edit_product(id=id, form_data=request.POST)
    return redirect(reverse('products'))

def cart(request):
    goods = {}
    for value, item in request.session['cart'].iteritems():
        good = Products.objects.get(pk=int(value))
        total = 25.00*item['quantity']
        my_list = {
                    'name':good.product,
                    'description':good.description,
                    'price':25.00,
                    'quantity':item['quantity'],
                    'total':total
                    }
        pk = str(good.id)
        goods[pk]=my_list
        print goods
        print ('*'*90)
    return render(request, 'ecommerce/cart.html', {'goods':goods})

def ship(request):
    return render(request, 'ecommerce/ship.html')
