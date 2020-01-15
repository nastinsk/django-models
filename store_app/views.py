from django.views.generic import ListView
from .models import Product

class HomePageView(ListView):
    template_name = 'home.html'
    model = Product

