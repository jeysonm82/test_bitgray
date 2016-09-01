"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app.views import APIListCreate
from app.models import Clientes, Compras, Productos, Sedes

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/clientes/$', APIListCreate.as_view(model=Clientes)),
    url(r'^api/clientes/(?P<pk>[0-9]{1,10})$', APIListCreate.as_view(model=Clientes) ),
    url(r'^api/compras/$', APIListCreate.as_view(model=Compras)),
    url(r'^api/compras/(?P<pk>[0-9]{1,10})$', APIListCreate.as_view(model=Compras) ),
    url(r'^api/productos/$', APIListCreate.as_view(model=Productos)),
    url(r'^api/productos/(?P<pk>[0-9]{1,10})$', APIListCreate.as_view(model=Productos) ),
    url(r'^api/sedes/$', APIListCreate.as_view(model=Sedes)),
    url(r'^api/sedes/(?P<pk>[0-9]{1,10})$', APIListCreate.as_view(model=Sedes) ),
]
