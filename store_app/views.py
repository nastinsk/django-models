from django.views.generic import ListView, DetailView
from .models import Product

class HomePageView(ListView):
    template_name = 'home.html'
    model = Product
    context_object_name = 'products'

class ProductDetailView(DetailView):
    template_name = 'product_detail.html'
    model = Product


