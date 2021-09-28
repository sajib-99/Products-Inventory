from django.contrib import admin
from django.urls  import path , include
from .import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'Pharmaceuticals'

urlpatterns = [
    path('', views.Pharmaceuticals, name ='Pharmaceuticals'),
    path('<str:url>/', views.brands, name ='brands'),
    path('<str:url>/<int:id>/', views.productdetails, name ='productdetails'),
    
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)