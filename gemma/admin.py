from django.contrib import admin
from gemma.models import Producers, Resellers,  Pricelist, Promotional, PricelistMain, PromotionalMain

# Register your models here.

class ProducersAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'address', 'zipcode', 'city', 'phone', 'phones', 'fax', 'email')

class ResellersAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'address', 'zipcode', 'city', 'phone', 'phones', 'fax', 'email')
    list_filter = ('producers', )


class PricelistMainAdmin(admin.ModelAdmin):
    list_display = ('name', 'date',)


class PricelistAdmin(admin.ModelAdmin):
    list_display = ('pricelist_name', 'pricelist_detail', 'created',)
    list_filter = ('pricelist_main', )

class PromotionalAdmin(admin.ModelAdmin):
    list_display = ('promotional_name', 'promotional_detail', 'created',)
    list_filter = ('promotional_main', )


class PromotionalMainAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', )




admin.site.register(Promotional, PromotionalAdmin)
admin.site.register(Pricelist, PricelistAdmin)
admin.site.register(Producers, ProducersAdmin)
admin.site.register(Resellers, ResellersAdmin)
admin.site.register(PricelistMain, PricelistMainAdmin)
admin.site.register(PromotionalMain, PromotionalMainAdmin)


