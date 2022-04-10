from ast import Return
from urllib import response
from rest_framework.response import Response
from rest_framework.views import APIView

from commodity.models import (
    Commodity_images,
    Commodity_type,
    Commodity,
)

from .models import Organization, Faq, Contacts
from picture.models import Picture_type, Pictures

from .serializers import (
    ContactsList, 
    OrganizationList, 
    FaqList, 
    Picture_typeList,
    CommodityImgList,
    CommodityTypeList,
    CommodityList,
    PicturesList,
)
from organization import serializers



class OrganizationView(APIView):
    def get(self, request):
        try:
            org = Organization.objects.all()
            serializer = OrganizationList(org,many=True)
            return Response(serializer.data)
        except:
            return Response({"errors":"Hatolik bor"})


class FaqView(APIView):
    def get(self, request):
        try:
            faq = Faq.objects.all()
            serializer = FaqList(faq, many=True)
            return Response(serializer.data)
        except:
            return Response({"errors":"Hatolik bor"})


class Picture_typeView(APIView):
    def get(self, request):
        try:
            type = Picture_type.objects.all()
            serializer = Picture_typeList(type, many=True)
            return Response(serializer.data)
        except:
            return Response({"errors":"Hatolik bor"})


class PictureView(APIView):
    def get(self, request):
        try:
            img = Pictures.objects.all()
            serializer = PicturesList(img, many=True)
            return Response(serializer.data)
        except:
            return Response({"errors":"Hatolik bor"})

class ContactsView(APIView):
    def post(self,request):
        review = ContactsList(data=request.data)
        if review.is_valid():
            review.save()
        return Response(status=201)


class Contact(APIView):
    def get(self, request):
        try:
            con = Contacts.objects.all()
            serializers = ContactsList(con, many=True)
            return Response(serializers.data)
        except:
            return Response({"errors":"Hatolik bor"})

class CommodityImgView(APIView):
    def get(self, request):
        try:
            comimg = Commodity_images.objects.all()
            serializer = CommodityImgList(comimg, many = True)
            return Response(serializer.data)
        except:
            return Response({"error": "Hatolik bor"})


class CommodityTypeView(APIView):
    def get(self, request):
        try:
            comtyp = Commodity_type.objects.all()
            serializer = CommodityTypeList(comtyp, many = True)
            return Response(serializer.data)
        except:
            return Response({"error": "Hatolik bor"})


class CommodityView(APIView):
    def get(self, request):
        try:
            com = Commodity.objects.all()
            serializer = CommodityList(com, many = True)
            return Response(serializer.data)
        except:
            return Response({"error": "Hatolik bor"})