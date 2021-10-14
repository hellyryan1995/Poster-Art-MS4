
from django.db import models
from multiselectfield import MultiSelectField


class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    # SIZE_POSTER = (
    #     ('A4: 21.0 x 29.7cm', 'A4: 21.0 x 29.7cm'),
    #     ('A3: 29.7 x 42.0cm', 'A3: 29.7 x 42.0cm'),
    #     ('A2: 42.0 x 59.4cm', 'A2: 42.0 x 59.4cm'),
    # )

    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    # size = MultiSelectField(
    #     choices=SIZE_POSTER, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

