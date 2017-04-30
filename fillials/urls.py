"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from fillials.views import *


urlpatterns = [
    url(r'^$', salon, name='salon'),
    url(r'^list/$', list_of_salons, name='list_of_salons'),
    url(r'^list/(?P<salon_id>[0-9]+)/$', salon_detail, name='salon_detail'),
    url(r'^edit/$', edit_salon, name='edit_salon'),
    url(r'^create/$', create_salon, name='create_salon'),
    url(r'^list_of/$', list_of_salons_to_activate, name='list_of_salons_to_activate'),
    url(r'^activate/(?P<salon_id>[0-9]+)/$', activate_salon, name='activate_salon'),
    url(r'^create_gallery/$', create_gallery, name='create_gallery'),
    url(r'^delete_gallery/(?P<id_image>[0-9]+)/$', delete_gallery, name='delete_gallery'),
    url(r'^edit_gallery/(?P<id_image>[0-9]+)/$', edit_gallery, name='edit_gallery'),
    url(r'^create_service/$', create_service, name='create_service'),
]
