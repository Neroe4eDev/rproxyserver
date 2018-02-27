from django.shortcuts import render
from django.core.urlresolvers import reverse
from revproxy.views import ProxyView
from django.http import HttpResponse
from django.views.generic import View

class TestProxyView(ProxyView):
    
    upstream = "http://dream.msh.org"
    rewrite = (
        (r'^/index/moz', r'http://www.mozilla.org'),
        (r'^/index/google', r'http://google.com'),
        (r'^/index/header', r'http://localhost:8000/header')
    )

    def get_proxy_request_headers(self, request):
        headers = super(TestProxyView, self).get_proxy_request_headers(request)
        headers['WHOIS'] = 'EHEALTH4SOMEONE'
        return headers
    
    def get(self, request, *args, **kwargs):
        return HttpResponse("nothing")

class NormalView(View):

    def get(self, request):
        response = HttpResponse()
        request.META['Age'] = "Custom Header"
        return response(request.META['Age'])
        