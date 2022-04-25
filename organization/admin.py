
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Organization, Faq, Contacts
from picture.models import (
    Pictures,
    Picture_type,
)
from emp.models import (
    Departament,
    Position,
    EMP,
)
from order.models import(
Product,
Order,
Order_detail,
Client,
Pay,
Shiper,
)
from commodity.models import (
Commodity_type,
Commodity,
)


   


    
@admin.register(Organization)
class OrganizationAdmin(TranslationAdmin):
    
    pass
    


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
     list_display = ("name", "number")

# @admin.register(EMP)
# class EMPAdmin(TranslationAdmin):
#     list_display = ('id','FIO', 'Tel')
#     list_display_links = ('FIO',)



@admin.register(Pictures)
class PicturesAdmin(TranslationAdmin):
     list_dispalay = ("name")
@admin.register(Picture_type)
class Picture_typeAdmin(admin.ModelAdmin):
     list_dispalay = ("name")
@admin.register(Departament)
class DepartamentAdmin(admin.ModelAdmin):
    list_dispaly = ("name",)
@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("name", "departament")

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("FIO", "Tel")
admin.site.register(Pay)
admin.site.register(Shiper)
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_dispalay = ("client_id", "SumProce","Status")
admin.site.register(Order_detail)
admin.site.register(Commodity_type)
@admin.register(Commodity)
class ComAdmin(TranslationAdmin):
    list_display = ()

admin.site.register(Product)
