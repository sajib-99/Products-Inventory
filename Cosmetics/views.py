from django.shortcuts import render
from Cosmetics.models import CosmeticsProductType, BrandName, ProductsDetail


# Create your views here.
def Cosmetics(request):
    items= CosmeticsProductType.objects.all()
    
    context={'items': items}    
    return render(request,'cosmetics.html', context)

def brands(request,url):
    items= CosmeticsProductType.objects.all()

    categories = CosmeticsProductType.objects.get(url=url)
    brands = BrandName.objects.filter(Type=categories)
    
    context={'items': items, 'categories': categories, 'brands': brands}    
    return render(request,'cbrands.html', context)

def productdetails(request, id, url):
    brands= BrandName.objects.all()

    categories = BrandName.objects.get(id=id)
    productdetails = ProductsDetail.objects.filter(brand = categories)
    
    
    context={'brands': brands, 'categories': categories, 'productdetails': productdetails}    
    return render(request,'cproductdetails.html', context)