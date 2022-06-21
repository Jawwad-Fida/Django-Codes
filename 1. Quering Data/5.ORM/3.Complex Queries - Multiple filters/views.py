from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F

# Import product class
from store.models import Product

# Create your views here.

# A view function takes in a request and returns a response. request --> response (request handler)

# render a template and return HTML to client

def say_hello(request):
    
    ### Complex Lookups using query objects - Applying multiple filters
    
    # 1. Products: inventory < 10 and price < 20
    query_set = Product.objects.filter(inventory__lt=10, unit_price__lt=20) # passing in multiple keyword arguments
    # or
    query_set = Product.objects.filter(inventory__lt=10).filter(unit_price__lt=20)
    
    # using OR operator --> using Q object, from django.db.models import Q
    # Q --> represents a query expression
    query_set = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20))
    
    # not operator --> using ~ operator
    query_set = Product.objects.filter(Q(inventory__lt=10) | ~Q(unit_price__lt=20))
    
    ### Refering using another field
    
    # Products: inventory = price
    # from django.db.models import F --> using F we can refer to a particular field
    query_set = Product.objects.filter(inventory=F('unit_price'))
    
    # we can also refer to fields in related table
    query_set = Product.objects.filter(inventory=F('collection__id'))

    dic = {'name': 'John', 'products': list(query_set)}
    return render(request, 'hello.html', dic) #http requet, template name, context: mapping of variables to template
 