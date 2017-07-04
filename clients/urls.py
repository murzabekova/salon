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
from clients.views import *


urlpatterns = [
    url(r'^contacts/(?P<id_services>[0-9]+)/$', contacts, name="contacts"),
    url(r'^email/$', SubscriptionView, name="email"),
    url(r'^activation/(?P<id_client>[0-9]+)$', activation, name="activation"),
    url(r'^list_of_fillials/$', list_of_fillials, name="list_of_fillials"),
    url(r'^list_of_services/(?P<id_fillials>[0-9]+)/$', list_of_services, name="list_of_services"),
    url(r'^list_of_masters/(?P<id_services>[0-9]+)/$', list_of_masters, name="list_of_masters"),
    url(r'^event/(?P<id_master>[0-9]+)/$', event, name="event"),


]
