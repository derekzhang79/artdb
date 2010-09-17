# -*-*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('artworks.views',
    (r'range/(?P<year_from>\d+)/to/(?P<year_to>\d+)/$', 'in_range'),
    url(r'(?P<artwork_id>\d+)/$', 'artworks_record', name="artworks_record"),
    (r'(?P<artwork_id>\d+)/$', 'properties'),
    url(r'^$', 'artworks_list', name="artworks_list"),        
)
