from django.shortcuts import redirect, render , get_object_or_404 
from django.http import HttpResponse , HttpResponseRedirect
from django.http import Http404 
from django.urls import reverse
from produits.models import Produit 
from categorys.models import Category

from .forms import ProduitForm
# Create your views here.

def index (request) : 
    produits=Produit.objects.all() 
    context = {
        'produits' : produits ,
    }
    return render (request,'produits/index.html', context)

def detail (request , id ) : 
    try : 
        produit=Produit.objects.get(id=id) 
    except : 
        return render(request , 'produits/notFound.html') 
    context = {
        'produit' : produit ,
    }
    return render (request , 'produits/detail.html',context)

def new (request) : 

    categorys=Category.objects.all()
    context={
        'categorys':categorys
    }
    if request.method == "POST" : 
        produit= ProduitForm (request.POST) 
        if produit.is_valid() : 
            produit.save() 
            return redirect ('index') 
        else : 
            message="Your data is invalid" 
            context = {
                "message" : message,
                 "categorys":categorys
            }
            return render (request , 'produits/new.html' , context)
    else : 
        return render (request , 'produits/new.html',context0)


def edit(request , id ) : 
    try : 
        produit=Produit.objects.get(id=id) 
    except : 
        return render('index') 
    Produit_form=ProduitForm(request.POST or None , instance = produit )
    if Produit_form.is_valid() : 
        Produit_form.save() 
        return redirect('index')
    context = {
        'produit' : produit ,
    }
    return render (request , 'produits/edit.html',context)
def delete (request,id):
    try:
        produit=Produit.objects.get(id=id)
    except produit.DoesNotExist:
        return redirect('index')
    produit.delete()
    return redirect('index')   