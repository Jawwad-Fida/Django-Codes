from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

# A view function takes in a request and returns a response. request --> response (request handler)


# render a template and return HTML to client

def say_hello(request):
    dic = {'name': 'John'}
    return render(request, 'hello.html', dic) #http requet, template name, context: mapping of variables to template
