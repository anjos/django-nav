import os 
import settings
from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import direct_to_template 

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', direct_to_template, {'template': 'home.html'}),
    url(r'^admin/', admin.site.urls),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^jsi18n/(?P<packages>\S+?)/$', 
      'django.views.i18n.javascript_catalog'),
    url(r'^jsi18n/$', 'django.views.i18n.javascript_catalog'),
    url(r'^rosetta/', include('rosetta.urls')),
    url(r'^login/$', 'views.login', name='login'), 
    url(r'^logout/$', 'views.logout', name='logout'),

    # Media serving
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': settings.MEDIA_ROOT,
     'show_indexes': True},
     name='media'), 
    )
