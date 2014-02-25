from django.conf.urls import patterns, url

from gemma import views

urlpatterns = patterns('',
        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.login, name='login'),
        url(r'^pricelist/$', views.pricelist, name='pricelist'),
        url(r'^promotional/$', views.promotional, name='promotional'))






