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
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from homepage import views as homepage_views
from slider import views as slider_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', homepage_views.index, name='index'),
    url(r'^end/$', homepage_views.end, name='end'),
    url(r'^error/$', homepage_views.error, name='error'),
    url(r'^error/$', homepage_views.error, name='error'),

    url(r'^post/', include('post.urls')),

    url(r'^accounts/', include('accounts.urls')),
    url(r'^fillial/', include('fillials.urls')),
    url(r'^profile/', include('profiles.urls')),
    url(r'^clients/', include('clients.urls')),
    url(r'^services/', include('services.urls')),
    url(r'^schedules/', include('schedules.urls')),

    url(r'^slider/$', slider_views.show, name='slider'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
