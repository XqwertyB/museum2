from importlib.metadata import files
from rest_framework import serializers
from .models import Organization, Faq, Contacts
from picture.models import Picture_type, Pictures
from commodity.models  import  Commodity_type, Commodity


class OrganizationList(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields ='__all__'

class FaqList(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = '__all__'



class Picture_typeList(serializers.ModelSerializer):
    class Meta:
        model = Picture_type
        fields = '__all__'


class PicturesList(serializers.ModelSerializer):
    class Meta:
        model = Pictures
        fields = '__all__'

class ContactsList(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'




class CommodityTypeList(serializers.ModelSerializer):
    class Meta:
        model = Commodity_type
        fields = '__all__'

class CommodityList(serializers.ModelSerializer):
    class Meta:
        model = Commodity
        fields = '__all__'