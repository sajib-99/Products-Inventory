from django.contrib import admin

from DailyNeeds.models import DailyNeedsProductType, dBrands, ProductsDetails

class DailyNeedsProductTypeAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'image')
admin.site.register(DailyNeedsProductType,DailyNeedsProductTypeAdmin)

class dBrandsAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'Type', 'image')
admin.site.register(dBrands,dBrandsAdmin) 

class ProductsDetailsAdmin(admin.ModelAdmin):
    
    list_display = ('Type', 'brand', 'image')
admin.site.register(ProductsDetails,ProductsDetailsAdmin) 

