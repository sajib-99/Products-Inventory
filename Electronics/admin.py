from django.contrib import admin

from Electronics.models import ProductType
from Electronics.models import Brands
from Electronics.models import ModelNo
from Electronics.models import ProductDetails


# Register your models here.
class ProductTypeAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'image')
admin.site.register(ProductType,ProductTypeAdmin)

class BrandsAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'Type', 'image')
admin.site.register(Brands,BrandsAdmin) 


class ModelNoAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'brand', 'Type')
admin.site.register(ModelNo,ModelNoAdmin) 

class ProductDetailsAdmin(admin.ModelAdmin):
    
    list_display = ('ModelNo', 'brand', 'image')
admin.site.register(ProductDetails,ProductDetailsAdmin) 