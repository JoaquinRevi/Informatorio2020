from django.urls import path

from ProyectoPongoApp import views
from ProyectoPongo.settings import base
from django.conf.urls.static import static

urlpatterns = [

    path("Nosotros",views.nosotros, name = "nosotros"),
    path("Ayuda",views.ayuda, name = "ayuda"),
    ]

urlpatterns += static(base.MEDIA_URL, document_root = base.MEDIA_ROOT)