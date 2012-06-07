from django.contrib import admin
from models import AbuseReport

def make_accepted(modeladmin, request, queryset):
    queryset.update(accepted=True)
make_accepted.short_description = "Ustaw jako zaakceptowane"

class AbuseReportAdmin(admin.ModelAdmin):
    list_display = ('author',
                    'author_email',
                    'author_ip',
                    'admin_targeturl',
                    'created',
                    'accepted')

    list_filter = ('accepted',)
    ordering = ['-created']
    actions = [make_accepted]
admin.site.register(AbuseReport, AbuseReportAdmin)