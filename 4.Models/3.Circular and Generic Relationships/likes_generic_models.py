from django.db import models

from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.

class LikedItem(models.Model):
    # What user liked what object
    user = models.ForeignKey(User, on_delete=models.CASCADE) # if a user is deleted, then remove all the likes he/she has made on objects
    
    # Create a Generic relationship
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id= models.PositiveIntegerField()
    content_object = GenericForeignKey()



