from .import views
from django.contrib import admin
from django.urls  import path , include

from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'

admin.site.site_header = "SheBa Enterprises"
admin.site.site_title = "SheBa Enterprises"

urlpatterns = [
    
    path('', views.index , name = 'index'),
    path('about', views.about , name = 'about'),
    path('mission', views.mission , name = 'mission'),
    path('vision', views.vision , name = 'vision'),
    path('partners', views.partners , name = 'partners'),
    path('career', views.career , name = 'career'),
    path('faq', views.faq , name = 'faq'),
    path('clientform', views.clientform , name = 'clientform'),
    path('quote', views.quote , name = 'quote'),
    path('policy', views.policy , name = 'policy'),
    path('contact', views.contact , name = 'contact'),
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)