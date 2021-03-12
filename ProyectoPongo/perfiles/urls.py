from django.urls import path
from . import views
from ProyectoPongo.settings import base
from django.conf.urls.static import static

urlpatterns = [
    path('registro',views.register, name = "registro"),
    path('login',views.login, name = "login"),
    path('logout',views.logout, name = "logout"),
    path('perfil',views.perfil, name = "perfil"),
    path('perfiledit',views.perfiledit, name = "perfiledit")
    ] 

urlpatterns += static(base.MEDIA_URL, document_root = base.MEDIA_ROOT)
