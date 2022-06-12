from django.db import models

# Create your models here.

# models.Model --> base class for all models
# django field types --> google it
# every field types has field options
# Django automatically creates id field automically for each model class which will be a PK
# primary_key=True --> if u want to set manually
 
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField() #longtext
    price = models.DecimalField(max_digits=6, decimal_places=2) #e.g 9999.99
    inventory = models.IntegerField() #int
    last_update = models.DateTimeField(auto_now=True) # stores current datetime
    #also auto_now_add
    
class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'
    
    #choices --> ('value in db','human readable value')
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold'),  
    ]
    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True) # unique email
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    
    # limit the list of values for a field --> choices
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)
    
class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'
    
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING,'Pending'),
        (PAYMENT_STATUS_COMPLETE,'Complete'),
        (PAYMENT_STATUS_FAILED,'Failed'),
    ]
    
    #customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    placed_at = models.DateTimeField(auto_now_add=True) # stores current datetime 
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)
     