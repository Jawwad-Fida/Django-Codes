from unittest import result
from django.forms import DecimalField
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Value, Func, Count, ExpressionWrapper
from django.db.models.aggregates import Max, Min, Avg, Sum
from django.db.models.functions import Concat
# Import product class
from store.models import Product, OrderItem, Order, Customer

# Create your views here.

# A view function takes in a request and returns a response. request --> response (request handler)

# render a template and return HTML to client

def say_hello(request):
    
    ### Grouping Data
    
    # from django.db.models import Count
    # Q) number of orders placed by each customer
    # Django will create an order_set field in Customer Class (as customer is Fk in order class) [reverse relationship]
    queryset = Customer.objects.annotate(orders_count=Count('order')) # Left JOIN
    # But only for Count method, u have to specify field name without set
    
    ### Expression Wrappers
    
    # Expression class is the main class. Derived classes: Value, F, Func, Aggregate, ExpressionWrapper
    # We use ExpressionWrapper class when building complex expressions
    
    # say we want to give our Product class a new field(although temporary) 
    # from django.db.models import ExpressionWrapper
    
    # specify type of outputfield
    discounted_price = ExpressionWrapper(F('unit_price') * 0.8, output_field=DecimalField())
    queryset = Product.objects.annotate(discounted_price=discounted_price) 
    
    
    

    dic = {'name': 'John', 'products': list(queryset)}
    return render(request, 'hello.html', dic) #http requet, template name, context: mapping of variables to template
 