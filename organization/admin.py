from cProfile import label
from tkinter import Widget
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
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

class AdminForms(forms.ModelForm):
    discription_ru = forms.CharField(label="описание", Widget=CKEditorUploadingWidget())
    discription_en = forms.CharField(label="описание", Widget=CKEditorUploadingWidget())
    discription_uz = forms.CharField(label="описание", Widget=CKEditorUploadingWidget())


    class Meta:
        model = Commodity
        fields = '__all__'
    
@admin.register(Organization)
class OrganizationAdmin(TranslationAdmin):
    list_display = ("id", "name", "tel_number1",)
    list_display_links = ("name",)

@admin.register(Faq)
class FaqAdmin(TranslationAdmin):
    list_display = ("query",)

@admin.register(Contacts)
class ContactsAdmin(TranslationAdmin):
    list_display = ("name", "number")

@admin.register(EMP)
class EMPAdmin(TranslationAdmin):
    list_display = ('id','FIO', 'Tel')
    list_display_links = ('FIO',)



@admin.register(Pictures)
class PicturesAdmin(TranslationAdmin):
    list_dispalay = ("name")
@admin.register(Picture_type)
class Picture_typeAdmin(TranslationAdmin):
    list_dispalay = ("name")
@admin.register(Departament)
class DepartamentAdmin(TranslationAdmin):
    list_dispaly = ("name",)
@admin.register(Position)
class PositionAdmin(TranslationAdmin):
    list_display = ("name", "departament")

@admin.register(Client)
class ClientAdmin(TranslationAdmin):
    list_display = ("FIO", "Tel")
admin.site.register(Pay)
admin.site.register(Shiper)
@admin.register(Order)
class OrderAdmin(TranslationAdmin):
    list_dispalay = ("client_id", "SumProce","Status")
admin.site.register(Order_detail)
admin.site.register(Commodity_type)
@admin.register(Commodity)
class ComAdmin(TranslationAdmin):
    list_display = ('name','buy_or_not','type')

admin.site.register(Product)
