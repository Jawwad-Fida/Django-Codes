from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

# A view function takes in a request and returns a response. request --> response (request handler)

def say_hello(request):
    return HttpResponse('Hello World!')
