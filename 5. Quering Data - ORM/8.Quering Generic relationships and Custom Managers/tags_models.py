from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


# custom class for all managers (custom manager - replaces default manager of object)
class TaggedItemManager(models.Manager):
    def get_tags_for(self, obj_type, obj_id):
        # Querying Generic Relationships

        # ContentType is a model class --> get_for_models() a special manager object just for this class
        content_type = ContentType.objects.get_for_models(obj_type)
        # this is the content type id for the store.product model from django_content_type

        # Filter tag items
        # tag_id is a FK to tags table. The actual tags are over there, so we need to preload this field
        # otherwise we will end up a lot of extra queries to the database.
        queryset = TaggedItem.objects \
            .select_related('tag') \
            .filter(
                content_type=content_type,
                object_id=obj_id  # this is mostly passed from url. Product id that we want to query
            )
        # \ is for chaining methods in new lines

        return queryset


class Tag(models.Model):
    label = models.CharField(max_length=255)


class TaggedItem(models.Model):
    # Custom manager for object
    objects = TaggedItemManager()

    # What tag is applied to what object
    # if a tag is deleted, then all the objects it is applied to are deleted
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    # Creating Generic Relationships

    # Identify the object (in our application) the tag is added to
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
