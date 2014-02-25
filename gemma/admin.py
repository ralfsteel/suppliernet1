from django.contrib import admin
from gemma.models import Producers, Resellers, Userprofile, Pricelist, Promotional

# Register your models here.

class UserprofileAdmin(admin.ModelAdmin):
    list_display = ('user', )

class ProducersAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'address', 'zipcode', 'city', 'phone', 'phones', 'fax', 'email')

class ResellersAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'address', 'zipcode', 'city', 'phone', 'phones', 'fax', 'email')
    list_filter = ('producers', )

class PricelistAdmin(admin.ModelAdmin):
    list_display = ('pricelist_name', 'pricelist_detail')

class PromotionalAdmin(admin.ModelAdmin):
    list_display = ('promotional_name', 'promotional_detail')


admin.site.register(Userprofile, UserprofileAdmin)
admin.site.register(Promotional, PromotionalAdmin)
admin.site.register(Pricelist, PricelistAdmin)
admin.site.register(Producers, ProducersAdmin)
admin.site.register(Resellers, ResellersAdmin)
