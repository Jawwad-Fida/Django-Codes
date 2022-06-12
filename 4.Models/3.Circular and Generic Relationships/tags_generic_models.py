from django.db import models

# from store.models import Product
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.

# When we designed the Tag app, we did it to re-use it in any projects. 

class Tag(models.Model):
    label = models.CharField(max_length=255)

class TaggedItem(models.Model):
    # What tag is applied to what object
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE) # if a tag is deleted, then all the objects it is applied to are deleted
    
    # Creating Generic Relationships
    
    # Idenitify the object (in our application) the tag is added to
    # we need 1) Type of an object (product, video, article)
    # 2) ID of an object # 3) Content object
    
    # using ContentType (Built-in), we can create generic relationships with our models
    # ContentType represents the type of an object in our application
    
    # 1)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # 2)
    object_id = models.PositiveIntegerField()
    
    # Read the actual object the tag is applied to
    content_object = GenericForeignKey()
