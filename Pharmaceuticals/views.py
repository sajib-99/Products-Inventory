from django.shortcuts import render
from Pharmaceuticals.models import MedicineType, pBrands, medicine


# Create your views here.
def Pharmaceuticals(request):
    items= MedicineType.objects.all()
    
    context={'items': items}    
    return render(request,'pharmaceuticals.html', context)

def brands(request,url):
    items= MedicineType.objects.all()

    categories = MedicineType.objects.get(url=url)
    brands = pBrands.objects.filter(Type=categories)
    
    context={'items': items, 'categories': categories, 'brands': brands}    
    return render(request,'pbrands.html', context)

def productdetails(request, id, url):
    brands= pBrands.objects.all()

    categories = pBrands.objects.get(id=id)
    productdetails = medicine.objects.filter(brand = categories)
    
    
    context={'brands': brands, 'categories': categories, 'productdetails': productdetails}    
    return render(request,'pproductdetails.html', context)