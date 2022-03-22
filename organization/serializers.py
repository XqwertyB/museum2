from rest_framework import serializers
from .models import Organization, Faq


class OrganizationList(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields ='__all__'

class FaqList(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = '__all__'