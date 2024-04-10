from django.shortcuts import render
from django.views import generic

from Accesorios.models import Accesorio

# Create your views here.
class AccesorioView (generic.ListView):
    template_name = "accesorios/accesorios.html" # template
    context_object_name = "accesorios" # nombre de la variable en el template
    queryset = Accesorio.objects.all() # SELECT * FROM Accesorio
    
    