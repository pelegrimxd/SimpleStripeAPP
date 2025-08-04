from django.db import models
from django.db.models import CASCADE


# Create your models here.
class Item(models.Model):
    name = models.CharField(null=False)
    description = models.TextField(null=False)
    price = models.IntegerField(null=False)

    class Meta:
        db_table = 'Item'

class Order(models.Model):
    item = models.ForeignKey('Item', on_delete=CASCADE)

    class Meta:
        db_table = 'Order'