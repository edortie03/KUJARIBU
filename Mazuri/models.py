from django.db import models
class Customer (models.Model):
    full_name = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 50)

class Order(models.Model):
    STATUS_CHOICE=[
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('delivered', 'Delivered')
    ]
    oder_number = models.CharField(max_length=20,unique=True)
    customer_name = models.ForeignKey(Customer, on_delete = models.CASCADE)
    phone = models.CharField(max_length=50)

