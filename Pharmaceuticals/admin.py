from django.contrib import admin

# Register your models here.
from Pharmaceuticals.models import MedicineType, pBrands, medicine

class MedicineTypeAdmin(admin.ModelAdmin):
    
    list_display = ('name',)
admin.site.register(MedicineType,MedicineTypeAdmin)

class pBrandsAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'Type', 'image')
admin.site.register(pBrands,pBrandsAdmin) 

class medicineAdmin(admin.ModelAdmin):
    
    list_display = ('Type', 'brand', 'name')
admin.site.register(medicine,medicineAdmin) 
