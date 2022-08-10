from django.shortcuts import render

# Create your views here.
from .models import *
from .serializer import *
from sendsms import sendTelegram
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
class BasicPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({

            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'current_page_num': self.page.number,
            'all_pages': self.page.paginator.num_pages,
            'count': self.page.paginator.count,

            'results': data
        })
class MeViewset(ModelViewSet):
    queryset = Me.objects.all().order_by('-id')[:1]
    serializer_class = MeSerializer
    pagination_class = None
class SocialLinksViewset(ModelViewSet):
    queryset = SocialLinks.objects.all().order_by('-id')[:1]
    serializer_class = SocialLinksSerializer
    pagination_class = None
class PortfolioViewset(ModelViewSet):
    queryset = Portfolio.objects.all().order_by('-id')
    serializer_class = PortfolioSerializer
    pagination_class = BasicPagination

class SendMe(APIView):
    def post(self,request,name,email,message):
        text = f"⭐️Yangi Xabar⭐️\n" \
               f"Elektron pochta manzil: {email}\n" \
               f"Xabar yuborgan shaxs: {name}\n" \
               f"Xabar: {message}"

        sendTelegram(text)
        return Response({'status':'Ok'})
class Visitor(APIView):
    def get(self,request):
        try:
            visitorcha = Visitors.objects.get(id=1)
            visitorcha.visitor = visitorcha.visitor +1
            visitorcha.save()
        except Visitors.DoesNotExist:
            Visitors.objects.create(visitor=1)
        count = Visitors.objects.all().count()
        return Response({'visitors':count})
