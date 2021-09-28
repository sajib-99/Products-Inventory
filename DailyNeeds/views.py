from django.shortcuts import render
from DailyNeeds.models import DailyNeedsProductType, dBrands, ProductsDetails


# Create your views here.
def DailyNeeds(request):
    items= DailyNeedsProductType.objects.all()
    
    context={'items': items}    
    return render(request,'dailyneeds.html', context)

def brands(request,url):
    items= DailyNeedsProductType.objects.all()

    categories = DailyNeedsProductType.objects.get(url=url)
    brands = dBrands.objects.filter(Type=categories)
    
    context={'items': items, 'categories': categories, 'brands': brands}    
    return render(request,'dbrands.html', context)

def productdetails(request, id, url):
    brands= dBrands.objects.all()

    categories = dBrands.objects.get(id=id)
    productdetails = ProductsDetails.objects.filter(brand = categories)
    
    
    context={'brands': brands, 'categories': categories, 'productdetails': productdetails}    
    return render(request,'dproductdetails.html', context)