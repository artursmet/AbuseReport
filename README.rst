===========
AbuseReport
===========

Requirements
------------

- Django 1.3
- django-recaptcha


Installation
------------

- Clone repo and save abusereport directory in Your Django Project Dir
- Add 'abusereport' to INSTALLED_APPS in project settings
- Run 
    $ ./manage.py syncdb

Configuration
-------------

- Make sure that Your project has set DEFAULT_FROM_EMAIL variable in settings
- Set Email notification recipients:
    add following statement to project's settings:
        
        ``ABUSEREPORT_SENDTO = ['admin@host.com', 'admin2@host.com']``


Usage
-----

In Your Content model implement method content_type() that returns 
django.contrib.contenttypes.models.ContentType instance for this model.
eg.::

    @property
    def content_type(self):
        from django.contrib.contenttypes.models import ContentType
        return ContentType.objects.get_for_model(self)

On page template with Content add report button via templatetag:
obj is variable name for Model Instance.::

    {{ load abusereport_tags }}
    {% abuse_report_button obj.content_type.id obj.id %}

That's it. It should work.