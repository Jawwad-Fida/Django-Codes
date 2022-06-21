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
    
    ### Sorting
    # using order_by()
    
    # ascending order of titles
    query_set = Product.objects.order_by('title')
    
    # desceding order
    query_set = Product.objects.order_by('-title')
    
    # multiple keywords 
    query_set = Product.objects.order_by('unit_price', '-title')
      
    # by using reverse() --> unit_price is DESC, title in ASC
    query_set = Product.objects.order_by('unit_price', '-title').reverse()
    
    # we can also use orderby() after filter() as they are applied on queryset  objects
    query_set = Product.objects.filter(collection__id=1).order_by('unit_price')
    
    # returns a individual element (not queryset object)
    product = Product.objects.order_by('unit_price')[0]
    # or
    product = Product.objects.earliest('unit_price') # sort by unit price and get first element
    # we also have latest --> get last element after sorting in DESC order
    
    ### Limiting Data
    
    # e.g From 50 products, show only 5 in front page
    query_set = Product.objects.all()[:5] # 0, 1, 2, 3, 4
    
    # 5,6,7,8,9
    query_set = Product.objects.all()[5:10]
    

    dic = {'name': 'John', 'product': product}
    return render(request, 'hello.html', dic) #http requet, template name, context: mapping of variables to template
 