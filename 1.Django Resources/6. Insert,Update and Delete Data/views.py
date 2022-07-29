import collections
from unittest import result
from django.forms import DecimalField
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Value, Func, Count, ExpressionWrapper
from django.db.models.aggregates import Max, Min, Avg, Sum
from django.db.models.functions import Concat
from django.contrib.contenttypes.models import ContentType

# Import product class and other classes
from store.models import Product, OrderItem, Order, Customer, Collection
from tags.models import TaggedItem


# Create your views here.

# A view function takes in a request and returns a response. request --> response (request handler)

# render a template and return HTML to client

def say_hello(request):
    """
    So far we have been quering data, 

    so lets see how to insert data into the database
    """

    # Creating Objects

    collection = Collection()
    collection.title = 'Video Games'
    # featured_product field is optional
    collection.featured_product = Product(pk=1)  # or id=1
    # or collection.featured_product_id = 1
    collection.save()

    # or

    Collection.objects.create(title='Video Games', featured_product_id=1)

    # ---------------------------------------

    # Updating Objects

    # first read the data from the database
    collection = Collection.objects.get(pk=11)  # or id=11
    # Then update the fields u want to
    collection.title = 'Games'
    collection.featured_product = None
    collection.save()

    # Or
    Collection.filter(pk=11).objects.update(
        title='Games', featured_product=None)

    # ---------------------------------------

    # Deleting Objects

    # Delete single object
    collection = Collection(pk=11)
    collection.delete()

    # Delete multiple objects in queryset

    # e.g. Delete objects with id > 5
    Collection.objects.filter(id__gt=5).delete()

    dic = {'name': 'John'}
    # http requet, template name, context: mapping of variables to template
    return render(request, 'hello.html', dic)
