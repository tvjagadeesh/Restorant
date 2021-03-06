"""muypicky1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from restaurants.views import (
  HomeTemplateview,Restaurant_ListView,RestaurantDetailView,RestaurantCreateView)
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',TemplateView.as_view(template_name='home.html'),name='home'),
    #url(r'^restaurants/$',HomeTemplateview.as_view(template_name='restaurants/restaurants_list.html')),
    url(r'^restaurants/$',Restaurant_ListView.as_view(),name='restaurants'),
    url(r'^restaurants/create/$',RestaurantCreateView.as_view()),
    url(r'^restaurants/(?P<slug>[\w-]+)/$',RestaurantDetailView.as_view()),
#    url(r'^restaurants/(?P<rest_id>[0-9]+)/',RestaurantDetailView.as_view()),
    url(r'^contact/$',TemplateView.as_view(template_name='contact.html'),name='contact'),
    url(r'^about/$',TemplateView.as_view(template_name='about.html'),name='about'),

]
