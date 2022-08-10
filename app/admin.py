from django.contrib import admin
from .models import Me,SocialLinks,Visitors,Portfolio

# Register your models here.
class MeAdmin(admin.ModelAdmin):
    list_display = ['name','age','profession']
admin.site.register(Me,MeAdmin)
admin.site.register(SocialLinks)
admin.site.register(Visitors)
admin.site.register(Portfolio)