from django.db import models
#from django.db.models.signals import m2m_changed

# Create your models here.
class Product(models.Model):
  brand = models.CharField(max_length=50)
  description = models.TextField()
  image = models.ImageField(upload_to='products/', null=False, blank=False)
  price = models.IntegerField(default=0)
  price_offer = None

  def __str__(self):
    return self.description