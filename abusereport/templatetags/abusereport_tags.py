from django import template
from django.template.loader import render_to_string

register = template.Library()

@register.simple_tag
def abuse_report_button(content_type_id, target_id):
    return render_to_string('abusereport/report_button.dhtml',
                            {'content_type': content_type_id,
                             'target_id': target_id
                            }
                            )
abuse_report_button.is_safe = True