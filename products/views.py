from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category

# Create your views here.


def all_products(request):
    """ view all Posters """

    products = Product.objects.all()

    categories = None
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didnt enter any search criteria!")
                return redirect(reverse('home'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products= products.filter(queries)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    context = {
        'products': products,
        'current_categories': categories,
        'search_term': query,
    }

    return render(request, 'products/products.html', context)
