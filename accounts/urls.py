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
from accounts.views import *


urlpatterns = [
    url(r'^signin/$', signin, name='signin'),
    url(r'^signout/$', signout, name='signout'),
    url(r'^create_master/$', create_master, name='create_master'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^users/$', users_list, name='users'),
    url(r'^assign_to_administrator/(?P<username>\w+)/$', assign_to_administrator, name='assign_to_administrator'),
]
