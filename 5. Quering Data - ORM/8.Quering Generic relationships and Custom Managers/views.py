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
from store.models import Product, OrderItem, Order, Customer
from tags.models import TaggedItem


# Create your views here.

# A view function takes in a request and returns a response. request --> response (request handler)

# render a template and return HTML to client

def say_hello(request):

    # Querying Generic Relationships
    """
    * an app built in a django project have no idea that other apps exist.
    * sql --> django_content_type --> contains all apps and the modal classes they contain 

    from django.contrib.contenttypes.models import ContentType 
    from store.models import Product
    from tags.models import TaggedItem
    """
    # ContentType is a model class --> get_for_models() a special manager object just for this class
    content_type = ContentType.objects.get_for_models(Product)
    # this is the content type id for the store.product model from django_content_type

    # Filter tag items
    # tag_id is a FK to tags table. The actual tags are over there, so we need to preload this field
    # otherwise we will end up a lot of extra queries to the database.
    queryset = TaggedItem.objects \
        .select_related('tag') \
        .filter(
            content_type=content_type,
            object_id=1  # this is mostly passed from url. Product id that we want to query
        )
    # \ is for chaining methods in new lines

    # Custom Managers
    queryset = TaggedItem.objects.get_tags_for(Product, 1)

    """
    Replace the default manager with a customer manager in Tags\model.py
    """

    dic = {'name': 'John', 'products': list(queryset)}
    # http requet, template name, context: mapping of variables to template
    return render(request, 'hello.html', dic)
