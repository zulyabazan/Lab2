from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Producto

# Create your views here.
def home(request):
  return HttpResponse("Hola Mundo. Te encuentras en la página de inicio del Linio Express")

class ProductListView(ListView):
    model = Producto

class ProductDetailView(DetailView):
    model = Producto
