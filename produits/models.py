from django.db import models
from categorys.models import Category
# Create your models here.
class Produit (models.Model) : 
    label=models.CharField(max_length =200) 
    prix =models.CharField(max_length=200)
    qte = models.IntegerField(default=0)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=0)
    def __str__ (self) : 
        return self.label 
