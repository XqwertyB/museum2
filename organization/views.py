from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Organization, Faq
from .serializers import OrganizationList, FaqList


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