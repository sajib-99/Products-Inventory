from django.shortcuts import render
from Garments.models import GarmentsProductType, BrandsName, ProductDetail


# Create your views here.
def Garments(request):
    items= GarmentsProductType.objects.all()
    brands= BrandsName.objects.all()
   
    context= { 'items': items, 'brands': brands }
    return render(request,'garments.html', context)

def brands(request,url):
    items= GarmentsProductType.objects.all()

    categories = GarmentsProductType.objects.get(url=url)
    brands = BrandsName.objects.filter(Type=categories)
    
    context={'items': items, 'categories': categories, 'brands': brands}    
    return render(request,'gbrands.html', context)

def productdetails(request, id, url):
    brands= BrandsName.objects.all()

    categories = BrandsName.objects.get(id=id)
    productdetails = ProductDetail.objects.filter(brand = categories)
    
    
    context={'brands': brands, 'categories': categories, 'productdetails': productdetails}    
    return render(request,'gproductdetails.html', context)