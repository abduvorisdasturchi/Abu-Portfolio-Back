from rest_framework import  serializers
from .models import *
class MeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Me
        fields = "__all__"
class SocialLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLinks
        fields = "__all__"
class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = "__all__"