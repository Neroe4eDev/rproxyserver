from django.conf.urls import include, url
from django.contrib import admin
from proxyapp.views import TestProxyView

urlpatterns = [
    # Examples:
    # url(r'^$', 'rproxyserver.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<path>.*)$', TestProxyView.as_view()),
]
