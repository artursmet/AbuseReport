from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.sites.models import Site
from django.conf import settings


def send_html_email(recipients, subject_src, body_src, extra_context={},
                    from_email=None):
    """
    Sends email rendered from given HTML template.
    Parameters:
        Required:
        recipients - where we want send email (email address list)
        subject_src - E-mail subject template
        body_src - Template file name

        Optional:
        extra_context - dictionary with parameters required to render message
                        template
        from_email - Custom email address in "From" field
    """

    if not from_email:
        from_email = settings.DEFAULT_FROM_EMAIL
    if not isinstance(recipients, list):
        recipients = recipients.split()

    # Set current site URL in template
    current_site = Site.objects.get_current()
    extra_context['SITE'] = current_site

    subject = render_to_string(subject_src, extra_context)
    html_content = render_to_string(body_src, extra_context)
    # this strips the html, so people will have the text as well.
    text_content = strip_tags(html_content)

    # create the email, and attach the HTML version.
    msg = EmailMultiAlternatives(subject, text_content,
                                 from_email, recipients
                                 )
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def notify_admins(abusereport):
    """
    Sends email notification about new Abuse Report.
    Recipients are admins defined in settings.ABUSEREPORT_SENDTO list
    """
    for mail in settings.ABUSEREPORT_SENDTO:
        ## Each admin should recieve his own abuse report on email
        ## So recipients_list parameter contains only one email address.
        send_html_email(recipients=mail, 
                        subject_src="abusereport/email/new_report_sub.txt",
                        body_src="abusereport/email/new_report_body.html",
                        extra_context={'report':abusereport})