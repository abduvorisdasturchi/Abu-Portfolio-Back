from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('behzodadmin/owner/', admin.site.urls),
    path('api/v1/',include('app.urls'))
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
