from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

# Import product class
from store.models import Product

# Create your views here.

# A view function takes in a request and returns a response. request --> response (request handler)

# render a template and return HTML to client

def say_hello(request):
    
    # Filtering data
    # google --> query set API --> Field look ups
    
    # 1. find all products whos unit_price is 20
    query_set = Product.objects.filter(unit_price=20)
    
    # 2. more expensive than 20 dollars
    # keyword = value 
    query_set = Product.objects.filter(unit_price__gt=20) # we also have __lt, __lte, __gte, __ gte
    
    # 3. range(min, max)
    query_set = Product.objects.filter(unit_price__range=(20,30))
    
    # 4. all products in collection 1, 2, 3
    query_set = Product.objects.filter(collection__id__range=(1,2,3))
    
    # 5. Find all products that have coffee in their title --> icontains -- not case-sentitive, contains() -- case-sensitive
    query_set = Product.objects.filter(title__icontains='coffee')
    
    # 6. we also have __startswith, __endswith, as well as their case insensitive versions
    
    # Find all products that were updated in 2021
    query_set = Product.objects.filter(last_update__year=2021)
    
    # we also have for Dates --> __year, __month, __day, __hour, __minute, __second
    
    # 7. To get all products without their description
    query_set = Product.objects.filter(description__isnull=True)
    

    dic = {'name': 'John', 'products': list(query_set)}
    return render(request, 'hello.html', dic) #http requet, template name, context: mapping of variables to template
 