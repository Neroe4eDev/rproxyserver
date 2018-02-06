from django.shortcuts import render
from revproxy.views import ProxyView

class TestProxyView(ProxyView):
    upstream = "https://example.com"