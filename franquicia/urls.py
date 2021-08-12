from django.conf.urls import url
from .views import  verificar_tc, franquicia_detail, franquicia_list_create


urlpatterns = [
    #url(r'^franquicia$', franquiciaAPI),
    #url(r'^franquicia/([0-9]+)$', franquiciaAPI),
   
    
    url(r'^franquicia$', franquicia_list_create),
    url(r'^franquicia/([0-9]+)$', franquicia_detail),
    url(r'^verificar$', verificar_tc)
]