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
    # url(r'^services/$', list_of_services, name='list_of_services'),
    url(r'^edit/$', edit_salon, name='edit_salon'),
    url(r'^create/$', create_salon, name='create_salon'),
    url(r'^list_of/$', list_of_salons_to_activate, name='list_of_salons_to_activate'),
    url(r'^activate/(?P<salon_id>[0-9]+)/$', activate_salon, name='activate_salon'),
]
