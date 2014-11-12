# -*- coding: utf-8 -*-
"""
Created on Fri Nov 07 14:32:27 2014

@author: 10256603
"""

from django.conf.urls import url,patterns,include
from django.contrib import admin

from django.conf import settings

from django.conf.urls.static import static


urlpatterns = patterns('',
        url(r'^admin/',include(admin.site.urls)),
        url(r'^', include('items.urls')),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
