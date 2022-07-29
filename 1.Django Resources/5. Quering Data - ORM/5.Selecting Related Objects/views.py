from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F

# Import product class
from store.models import Product, OrderItem, Order

# Create your views here.

# A view function takes in a request and returns a response. request --> response (request handler)

# render a template and return HTML to client

def say_hello(request):
    
    ### Selecting Related Objects
    
    # 1) we use select_related() when the other of the relationship has only 1 instance. e.g Product -- Collection (1)
    #queryset = Product.objects.all() # causes a lot of problems due to 1000s sql queries when accessing different tables together
    queryset = Product.objects.select_related('collection').all()
    #queryset = Product.objects.select_related('collection__SomeOtherField').all()
    # select_related() --> Django creates a join relationship between the tables Products and Collections.
    
    # 1) we use prefetch_related() when the other of the relationship has more than 1 instance. e.g Product -- Promotions (n)
    queryset = Product.objects.prefetch_related('promotions').all() # Another Join Relationship between Products and Promotions
    
    # we can also combine select_related() and prefetch_related()
    queryset = Product.objects.prefetch_related('promotions').select_related('collection').all()
    
    #Q) Get the last 5 orders with their customer and items (including products) 
    # from store.models import Order --> import order class
    # -placed_at --> DESC order to get the latest orders
    queryset = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
    # Django will create a reverse relationship between the tables Orders and OrderItems (since order_item doesn't exist in the modal class)
    # so set --> orderitem_set --> name of target class_set
    # orderitem_set__product --> load products referenced in OrderItems (select target field) 
    
    
    
    

    dic = {'name': 'John', 'products': list(queryset)}
    return render(request, 'hello.html', dic) #http requet, template name, context: mapping of variables to template
 