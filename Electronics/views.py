from django.shortcuts import render, get_object_or_404
from Electronics.models import ProductType
from Electronics.models import Brands
from Electronics.models import ModelNo
from Electronics.models import ProductDetails


# Create your views here.
def Electronics(request):
    
    items= ProductType.objects.all()
    brands= Brands.objects.all()
   
    context= { 'items': items, 'brands': brands }
    return render(request,'electronics.html', context)

def brands(request,url):
    items= ProductType.objects.all()

    categories = ProductType.objects.get(url=url)
    brands = Brands.objects.filter(Type=categories)
    
    context={'items': items, 'categories': categories, 'brands': brands}    
    return render(request,'brands.html', context)

def models(request, id, url):
    brands= Brands.objects.all()
    items= ProductType.objects.all()

    categories = Brands.objects.get(id=id)
    models = ModelNo.objects.filter(brand = categories)
    
    
    context={'brands': brands, 'categories': categories, 'models': models, 'items': items}    
    return render(request,'models.html', context)

def productdetails(request, id, url, uid):
    brands= Brands.objects.all()

    categories = ModelNo.objects.get(uid=uid)
    productdetails = ProductDetails.objects.filter(ModelNo = categories)
    
    
    context={'brands': brands, 'categories': categories, 'productdetails': productdetails}    
    return render(request,'productdetails.html', context)