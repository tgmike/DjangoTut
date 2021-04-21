from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120) #max_length= is required
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10000, decimal_places=2)
    summary = models.TextField(blank=False, null=False)
    featured = models.BooleanField() #null=True (Means field can be left empty) or default=True (Value set to true automatically) or run as is and handle it in the console