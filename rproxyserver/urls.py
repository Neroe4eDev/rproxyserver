from django.conf.urls import include, url
from django.contrib import admin
from proxyapp.views import TestProxyView, NormalView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^/', include(proxyapp.urls)),
    url(r'^index/(?P<path>.*)$', TestProxyView.as_view(), name='index-url'),
    # url(r'^(?P<path>.*)/header/$', NormalView.as_view(), name='normal-url'),
    url(r'^header/$', NormalView.as_view(), name='normal-url'),
]