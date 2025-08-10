from django.db import models
from django.db.models import CASCADE


# Create your models here.
class Item(models.Model):
    """Модель товара"""
    name = models.CharField(null=False)
    description = models.TextField(null=False)
    price = models.IntegerField(null=False)

    class Meta:
        db_table = 'Item'