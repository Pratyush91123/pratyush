from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Cart(models.Model):
    cart_id = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()
    instruction = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
    