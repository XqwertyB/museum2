from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Organization, Faq
from picture.models import Picture_type, Pictures

from .serializers import OrganizationList, FaqList, Picture_typeList


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
            serializer = Picture_typeList(img, many=True)
            return Response(serializer.data)
        except:
            return Response({"errors":"Hatolik bor"})

