from django.db import models

# Create your models here.
item_choice=(
    ("veg", "veg"),
    ("non-veg", "non-veg"),
    ("egg","egg")
    )
class Item(models.Model):
    item_name = models.CharField(max_length=50)
    item_price = models.IntegerField()
    item_description = models.CharField(max_length=200)
    item_type = models.CharField(choices=item_choice, max_length=100)
    item_image = models.ImageField()
    def __str__(self):
        return self.item_name