## Django Reverse Proxy Server

Navigate to http://169.48.64.219:8001

## Setting up the django-revproxy librrary

### Installation

This guide assumes you have django >= 1.8 installed.

```bash
$ pip install django-revproxy
```

### Configuration
After installation, you’ll need to configure your application to use django-revproxy. Start by adding `revproxy` to your `settings.py` file as follows:

```python
#Add 'revproxy' to INSTALLED_APPS.
INSTALLED_APPS = (
    # ...
    'django.contrib.auth',
    'revproxy',
    # ...
)
```

Next, you’ll need to create a View that extends `revproxy.views.ProxyView` and set the upstrem attribute:
The upstream attribute is the url you are reverse proxy-ing to. In this case we are using example.com

```python
from revproxy.views import ProxyView

class TestProxyView(ProxyView):
    upstream = 'http://example.com'
```
And now add your view in the `urls.py`:

```python
from myapp.views import TestProxyView

urlpatterns = patterns('',
    url(r'^(?P<path>.*)$', TestProxyView.as_view()),
)
```

Alternatively you could just use the default `ProxyView` as follow:

```python
from revproxy.views import ProxyView

urlpatterns = patterns('',
    url(r'^(?P<path>.*)$', ProxyView.as_view(upstream='http://example.com/')),
)
```
After starting your test server you should see the content of http://example.com/ on http://localhost:8000/.