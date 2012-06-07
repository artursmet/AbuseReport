# Create your views here.
from forms import AbuseReportForm
from models import AbuseReport
from django.http import HttpResponseForbidden, HttpResponse
from django.views.generic.simple import direct_to_template
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
import django.utils.simplejson as json
from django.template.loader import render_to_string
from django.template import RequestContext
from django.contrib.sites.models import Site
from helpers import notify_admins

def report_form(request, content_type, object_id):
    """
    Shows Report Form to User.
    Handles both POST and GET requests.
    When used via POST:
        - Validates AbuseReportForm
        - Saves content type and target id
        - Saves User's IP
        - Sends abuse notification for Admins
    via GET:
        - Renders template with blank AbuseReportForm
    """
    
    ct = get_object_or_404(ContentType, pk=content_type)
    target_model = ct.model_class()
    target = get_object_or_404(target_model, pk=object_id)
    current_site = Site.objects.get_current()

    if request.method == 'POST':
        form = AbuseReportForm(request.POST)
        if form.is_valid():
            # do magic
            f = form.save(commit=False)
            f.content_type = ct
            f.object_id = object_id
            f.author_ip = request.META.get("REMOTE_ADDR")
            f.save()
            ## notify admins
            notify_admins(f)
            return direct_to_template(request,
                                      "abusereport/thankyou.dhtml",
                                      {'report' : form }
                                      )
        else:
            # display errors
            return direct_to_template(request,
                              "abusereport/report_form.dhtml",
                              {'form': form}
                              )
    else:
        form = AbuseReportForm(initial={
                                    'target': target,
                                    'content_type': ct,
                               })

    return direct_to_template(request,
                              "abusereport/report_form.dhtml",
                              {'form': form, 'SITE':current_site}
                              )