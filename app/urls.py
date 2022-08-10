from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('me',MeViewset)
router.register('social',SocialLinksViewset)
router.register('portfolio',PortfolioViewset)
urlpatterns = [
    path('',include(router.urls)),
    path('sendtelegram/<str:name>/<str:email>/<str:message>/',SendMe.as_view()),
    path('visitor',Visitor.as_view())
]