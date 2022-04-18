from modeltranslation.translator import register, TranslationOptions
from .models import (
    Organization,
)
from commodity.models import Commodity, Commodity_type
from picture.models import Picture_type, Pictures


@register(Organization)
class OrganizationTranslationOptions(TranslationOptions):
    fields = ('name', 'info')


@register(Commodity)
class CommodityTranslationOptions(TranslationOptions):
    fields = ('name', 'info', 'author')


@register(Commodity_type)
class OrganizationTranslationOptions(TranslationOptions):
    fields = ('name', )

@register(Picture_type)
class Picture_typeTranslationOptions(TranslationOptions):
    fields = ('name', )

@register(Pictures)
class PicturesTranslationOptions(TranslationOptions):
    fields = ('name', 'title' )