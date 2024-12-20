# product/models.py
from django.db import models
import uuid


class DrugEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    name = models.CharField(max_length=63)
    desc = models.TextField()
    category = models.CharField(max_length=63)
    drug_type = models.CharField(max_length=31)
    drug_form = models.CharField(max_length=31)
    price = models.IntegerField()
    image = models.ImageField(upload_to='drugs/')  # Added specific upload directory

    class Meta:
        verbose_name_plural = "Drug Entries"
        ordering = ['name']  # Optional: mengurutkan berdasarkan nama

    shops = models.ManyToManyField('shop.ShopProfile', related_name='ShopDrug')

    def __str__(self):
        return self.name
