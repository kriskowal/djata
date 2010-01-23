
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^(?:\.(?P<format>[^/]*)|/|)$', 'djata.views.respond'),
    (r'^/(?P<view_name>[^/\.]*)(?=/|\.)', include('djata.urls_model')),
)

