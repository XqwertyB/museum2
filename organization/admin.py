from django.contrib import admin
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
Commodity_images,
Commodity_type,
Commodity,
)
@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "tel_number1",)
    list_display_links = ("name",)

@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ("query",)

@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ("name", "number")

@admin.register(EMP)
class EMPAdmin(admin.ModelAdmin):
    list_display = ('id','FIO', 'Tel')
    list_display_links = ('FIO',)



@admin.register(Pictures)
class PicturesAdmin(admin.ModelAdmin):
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
@admin.register(Pay)
class PayAdmin(admin.ModelAdmin):
    list_display = ("name")
@admin.register(Shiper)
class ShiperAdmin(admin.ModelAdmin):
    list_dispaly = ("FIO", "TEL")
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_dispalay = ("client_id", "SumProce","Status")
@admin.register(Order_detail)
@admin.register(Commodity_images)
@admin.register(Commodity_type)
@admin.register(Commodity)
@admin.register(Product)
