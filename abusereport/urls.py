from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('abusereport.views',
    (r'report/(?P<content_type>\d+)/(?P<object_id>\d+)/$', 'report_form'),
)