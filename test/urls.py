import settings
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'django.views.generic.simple.direct_to_template',
      {'template': 'base.html'}, name='root'),
    url(r'^admin/(.*)', admin.site.root, name='admin'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^jsi18n/(?P<packages>\S+?)/$', 
      'django.views.i18n.javascript_catalog'),
    url(r'^jsi18n/$', 'django.views.i18n.javascript_catalog'),
    url(r'^rosetta/', include('rosetta.urls')),
    )
