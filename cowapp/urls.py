from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^vaches$', views.vaches, name='vaches'),
    url(r'^vaches/(?P<pk>[0-9a-zA-Z]+)/$', views.info_vache, name='info_vache'),
    #안 쓰는 url, 숨김
    url(r'^vaches/(?P<pk>[0-9a-zA-Z]+)/vache_senseur/$', views.vache_senseur, name='vache_senseur'),

    url(r'^alarmes$',views.alarmes, name='alarmes'),

    # Post urls
   url(r'^post_list/$', views.post_list, name='post_list'),
   url(r'^post_list/post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
   url(r'^post_list/post/new/$', views.post_new, name='post_new'),
   url(r'^post_list/post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
   url(r'^post_list/post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),

    # Contact info
   url(r'^contact$',views.contact, name='contact'),

]