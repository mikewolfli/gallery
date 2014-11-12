from django.conf.urls import patterns, include, url
#from django.contrib import admin
from settings import ROOT_URL

#from django.conf import settings
#from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gallery.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

#    url(r'^admin/', include(admin.site.urls)),
     url(r'^%s' % ROOT_URL[1:], include('gallery.real_urls')),
)
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
