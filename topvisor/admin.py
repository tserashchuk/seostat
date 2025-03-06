from django.contrib import admin
from topvisor.models import  *

class MonitoringGroupAdmin(admin.ModelAdmin):
    list_display = ('domain', 'project_id', 'region_index','group_id')

admin.site.register(MonitoringGroup, MonitoringGroupAdmin)
admin.site.register(MonitoringGroupResult,  admin.ModelAdmin)
