#coding: utf-8
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
# Create your models here.


class AbuseReport(models.Model):
    """
    Generic AbuseReport model.
    Anyone can report Abuse on any content in Project.
    """
    author = models.CharField(max_length=200, 
                              verbose_name = u'Imię i nazwisko')
    author_email = models.EmailField(verbose_name=u'E-mail')
    author_ip = models.IPAddressField(verbose_name=u'Adres IP')
    reason = models.CharField(max_length=200, 
                              verbose_name=u'Powód zgłoszenia')
    accepted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    # Generic Stuff
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    target = generic.GenericForeignKey()

    class Meta:
        ordering = ['-created']

    def __unicode__(self):
        return "%s %s" % (self.author, self.target)


    def admin_targeturl(self):
        return "<a href='%s'>%s</a>" % (self.target.get_absolute_url(), 
                                        self.target.get_absolute_url()
                                        )
    admin_targeturl.allow_tags = True
    admin_targeturl.short_description = "Target URL"