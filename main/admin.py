from django.contrib import admin
from .models import partner, Quote, Contact, Career, ClientOwnerForm, EmployeeOwnerForm


class partnerAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'image')
admin.site.register(partner,partnerAdmin)

admin.site.register(Quote)
admin.site.register(Contact)
admin.site.register(Career)
admin.site.register(ClientOwnerForm)
admin.site.register(EmployeeOwnerForm)