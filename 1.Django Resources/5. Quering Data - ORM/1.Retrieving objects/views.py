from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

# Import product class
from store.models import Product

# Create your views here.

# A view function takes in a request and returns a response. request --> response (request handler)

# render a template and return HTML to client

def say_hello(request):
    
    # Returning objects 
    
    # 1. all objects
    query_set = Product.objects.all()
    
    # 2. particular object. Returns an exception if does not exist
    try:
        product = Product.objects.get(id=1) # or pk=1 (primary key field)
    except ObjectDoesNotExist:
        return HttpResponse("Product does not exist")
    
    # 3. using filter and first. Returns None if does not exist in query set
    product = Product.objects.filter(id=1).first()
    
    # 4. Check if objects exist in our query set 
    exists = Product.objects.filter(id=1).exists()
    
    # 
    dic = {'name': 'John'}
    return render(request, 'hello.html', dic) #http requet, template name, context: mapping of variables to template
 