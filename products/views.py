from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Product
from django.db.models import Q

# Create your views here.
class ProductListView(ListView):
  template_name = 'index.html'
  queryset = Product.objects.all().order_by('-id')
  paginate_by = 3

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    return context

class ProductSearchListView(ListView):
  template_name = 'products/search.html'
  paginate_by = 3

  def get_queryset(self):
    resultado = es_palindromo(self.query())
    if resultado and len(self.query()) > 3:
      filters = Q(brand__icontains=self.query()) | Q(description__icontains=self.query()) | Q(pk__iexact=self.query())
      productos = Product.objects.filter(filters)

      for product_search in productos:
        product_search.price_offer = int(product_search.price / 2)
      return productos

    if resultado and len(self.query()) <= 3:
      filters = Q(pk__iexact=self.query())
      productos = Product.objects.filter(filters)

      for product_search in productos:
        product_search.price_offer = int(product_search.price / 2)

      if not productos:
        filters = Q(brand__icontains=self.query()) | Q(description__icontains=self.query())
        productos = Product.objects.filter(filters)
        return productos
      return productos

    filters = Q(brand__icontains=self.query()) | Q(description__icontains=self.query()) | Q(pk__iexact=self.query())
    return Product.objects.filter(filters)

  def query(self):
    return self.request.GET.get('q')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['query'] = self.query()
    context['count'] = self.get_queryset().count()

    return context

def es_palindromo(busqueda):
  estandar = str(busqueda).lower().replace(' ', '')
  return estandar == estandar[::-1]
