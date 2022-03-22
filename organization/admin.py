from django.contrib import admin
from .models import Organization, Faq
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
class EMPAdmin(admin.ModelAdmin):
    list_display = ('FIO', 'Tel')

admin.site.register(Organization)
admin.site.register(Faq)
admin.site.register(Pictures)
admin.site.register(Picture_type)
admin.site.register(Departament)
admin.site.register(Position)
admin.site.register(EMP)
admin.site.register(Client)
admin.site.register(Pay)
admin.site.register(Shiper)
admin.site.register(Order)
admin.site.register(Order_detail)
admin.site.register(Commodity_images)
admin.site.register(Commodity_type)
admin.site.register(Commodity)
admin.site.register(Product)

