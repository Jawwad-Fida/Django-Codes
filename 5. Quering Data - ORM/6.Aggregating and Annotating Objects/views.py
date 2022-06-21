from unittest import result
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Value
from django.db.models.aggregates import Count, Max, Min, Avg, Sum

# Import product class
from store.models import Product, OrderItem, Order
from storefront.store.models import Customer

# Create your views here.

# A view function takes in a request and returns a response. request --> response (request handler)

# render a template and return HTML to client

def say_hello(request):
    
    ### Aggregating Objects
    # max,min, average, sum, count...
    
    # from django.db.models.aggregates import Count, Max, Min, Avg, Sum
    
    # id --> pk field 
    result_value = Product.objects.aggregate(Count('id')) 
    result_value = Product.objects.aggregate(count=Count('id')) # changing name of key from id from count
    
    result_value = Product.objects.aggregate(count=Count('id'),min_price=Min('unit_price'))
    
    # aggregate methods are applied on query sets
    result_value = Product.objects.filter(collection__id=1).aggregate(Count('id')) 
    
    ### Annotating Objects
    # add more fields to our objects when querying them (although temporary)
    
    # We can add fields by using expression objects and annotate method
    # from django.db.models import Q, F, Value
    
    queryset = Customer.objects.annotate(is_new=Value(True)) # is_new field created
    # or new_id = F('id') + 1 --> new_id field is created and set to id+1 of the object

    dic = {'name': 'John', 'products': list(queryset)}
    return render(request, 'hello.html', dic) #http requet, template name, context: mapping of variables to template
 