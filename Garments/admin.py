from django.contrib import admin

# Register your models here.
from Garments.models import GarmentsProductType, BrandsName, ProductDetail

class GarmentsProductTypeAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'image')
admin.site.register(GarmentsProductType,GarmentsProductTypeAdmin)

class BrandsNameAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'Type', 'image')
admin.site.register(BrandsName,BrandsNameAdmin) 

class ProductDetailAdmin(admin.ModelAdmin):
    
    list_display = ('Type', 'brand', 'image')
admin.site.register(ProductDetail,ProductDetailAdmin) 