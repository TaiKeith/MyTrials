from django.db import models

# Create your models here.
from django.urls import reverse

class Product(models.Model):
    title       = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(max_digits=10000, decimal_places=2)
    summary     = models.TextField()
    featured    = models.BooleanField(null=True) # default=True

    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"id": self.id}) #f"/products/{self.id}"
