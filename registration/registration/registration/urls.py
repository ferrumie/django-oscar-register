"""registration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import django
from django.apps import apps
import oscarapi.urls as oscarapp_api
urlpatterns = [
    path('admin/', admin.site.urls),
    # main app urls, to be linked with oscarapi endpoint
    path('api/', include('registerapp.urls')),
    # oscar api urls. contains login endpoint and ...
    path('api/', include(oscarapp_api)),
    # multiple language serve
    path('il8n/', include(django.conf.urls.i18n)),
    # Oscar urls (needed for oscar api)
    path('', include(apps.get_app_config('oscar').urls[0]))
]
