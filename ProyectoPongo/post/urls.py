from django.urls import path
from . import views
from ProyectoPongo.settings import base
from django.conf.urls.static import static


urlpatterns = [
    path('',views.inicio, name = "inicio"),
    path('categoria/<categoria_id>',views.categoria, name = "categoria"),
    path('crearpost',views.PostCreation, name = "crearpost")
    

    ]

urlpatterns += static(base.MEDIA_URL, document_root = base.MEDIA_ROOT)