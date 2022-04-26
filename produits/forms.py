from .models import Produit 
from django.forms import ModelForm 

class ProduitForm (ModelForm) : 
    class Meta : 
        model=Produit 
        fields='__all__'


