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

# Import product class and other classes
from store.models import Product, OrderItem, Order, Customer, Collection
from tags.models import TaggedItem


# Create your views here.

# A view function takes in a request and returns a response. request --> response (request handler)

# render a template and return HTML to client

# from django.db import transaction
# wrap the function inside a transaction
@transaction.atomic()
def say_hello(request):

    # Transactions
    # making multiple changes to database together, if one change fells, then all changes should be rollback

    # Parent
    order = Order()
    order.customer_id = 1
    order.save()

    item = OrderItem()
    item.order = order
    item.product_id = 1
    item.quantity = 1
    item.unit_price = 10
    item.save()

    dic = {'name': 'John'}
    # http requet, template name, context: mapping of variables to template
    return render(request, 'hello.html', dic)

# or


def say_hello2(request):

    # Transactions
    # making multiple changes to database together, if one change fells, then all changes should be rollback

    # .... some code (but we don't want this to wrapped inside a transaction)

    # return custom manager
    with transaction.atomic():
        # Parent
        order = Order()
        order.customer_id = 1
        order.save()

        item = OrderItem()
        item.order = order
        item.product_id = 1
        item.quantity = 1
        item.unit_price = 10
        item.save()
