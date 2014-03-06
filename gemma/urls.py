from django.conf.urls import patterns, url, include

from gemma import views

urlpatterns = patterns('',
        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.login, name='login'),
        url(r'^promotional/$', views.promotional, name='promotional'),
        url(r'^main_pricelist/$', views.main_pricelist, name='main_pricelist'),
        url(r'^(?P<plist_pk>\d+)/$', views.pricelist, name='gemma.pricelist'),
)







