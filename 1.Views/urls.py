# urls mapping for the project

from django.urls import path
from . import views

# . --> current directory

# urlpattern objects
urlpatterns = [
    path('hello/', views.say_hello) # passing reference to the functions.
]
