"""webchat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from web_chat.admin_panel import get_users, add_to_ban, delete_from_ban
from web_chat.views import Index, Login, Registration, Chat, Admin

urlpatterns = [
    #path('admin/', admin.site.urls),
    url(r'^$', Index.as_view(), name='index'),
    url(r'^login$', Login.as_view(), name='login'),
    url(r'^registration$', Registration.as_view(), name='registration'),
    url(r'^chat$', Chat.as_view(), name='chat'),
    url(r'^admin$', Admin.as_view(), name='admin'),
    url(r'^users$', get_users, name='getuser'),
    url(r'^addban$', add_to_ban, name='add_to_ban'),
    url(r'^delban/(\d+)$', delete_from_ban, name='delete_from_ban'),
]
