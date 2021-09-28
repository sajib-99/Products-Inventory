from django.contrib import admin

# Register your models here.
from Cosmetics.models import CosmeticsProductType, BrandName, ProductsDetail

class CosmeticsProductTypeAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'image')
admin.site.register(CosmeticsProductType,CosmeticsProductTypeAdmin)

class BrandNameAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'Type', 'image')
admin.site.register(BrandName,BrandNameAdmin) 

class ProductsDetailAdmin(admin.ModelAdmin):
    
    list_display = ('Type', 'brand', 'image')
admin.site.register(ProductsDetail,ProductsDetailAdmin) 