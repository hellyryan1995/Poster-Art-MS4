from django.shortcuts import render
from .models import Product, Category

# Create your views here.


def all_products(request):
    """ view all Posters """

    products = Product.objects.all()

    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    context = {
        'products': products,
        'current_categories': categories,
    }

    return render(request, 'products/products.html', context)
