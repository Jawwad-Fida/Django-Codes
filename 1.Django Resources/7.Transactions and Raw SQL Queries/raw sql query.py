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
from django.db import transaction
from django.db import connection

# Import product class and other classes
from store.models import Product, OrderItem, Order, Customer, Collection
from tags.models import TaggedItem


# Create your views here.

# A view function takes in a request and returns a response. request --> response (request handler)

# render a template and return HTML to client

def say_hello(request):

    # Executing RAW SQL Queries
    # raw() --> executes raw sql queries
    # These raw querysets are different. They dont have filter() or the rest...

    queryset = Product.objects.raw('SELECT * FROM store_product')
    queryset = Product.objects.raw('SELECT id, title FROM store_product')

    # or
    # bypass model layer
    # from django.db import connection
    with connection.cursor() as cursor:
        sql = "INSERT/SELECT/UPDATE"
        cursor.execute(sql)

    dic = {'name': 'John', 'result': list(queryset)}
    # http requet, template name, context: mapping of variables to template
    return render(request, 'hello.html', dic)
