from django.db import models

# Create your models here.
class Product(models.Model):
    name= models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    price = models.FloatField()
    file=models.FileField(upload_to='uploads')
    artist= models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class OrderDetail(models.Model):
    customer_email = models.EmailField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    stripe_payment_intent = models.CharField(max_length=250, null=True)
    has_paid = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)