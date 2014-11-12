# -*- coding: utf-8 -*-
"""
Created on Fri Nov 07 14:47:02 2014

@author: 10256603
"""

from django.conf.urls import patterns,url
from views import IndexView,Item_List_View,Item_Detail_View,Photo_Detail_View

urlpatterns = patterns('',
             url(r'^$',IndexView.as_view(),name = 'index'),
             url(r'^items/$', Item_List_View.as_view(),name ='item_list'),
             url(r'^items/(?P<pk>\d+)/$', Item_Detail_View.as_view(), name ='item_detail'),
             url(r'^photos/(?P<pk>\d+)/$',Photo_Detail_View.as_view(), name='photo_detail'),
             )