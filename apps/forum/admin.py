from django.contrib import admin
from import_export.admin import ExportActionModelAdmin
from .models import *


# Forum admin
class ForumAdmin(ExportActionModelAdmin,admin.ModelAdmin):
    # actions = [export_to_excel]
    list_display = ('title', 'description', 'created', 'modified')
    list_filter = ('created', 'modified')
    search_fields = ('title', 'description', 'organization__title')

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'modified')
    list_filter = ('created', 'modified')
    search_fields = ('title',)


class ForumProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'context', 'created', 'modified')
    list_filter = ('created', 'modified')
    search_fields = ('title', 'subtitle', 'context')


class EventAdmin(admin.ModelAdmin):
    list_display = ('day', 'date', 'created', 'modified')
    list_filter = ('created', 'modified')
    search_fields = ('day', 'date')


class EventTimeAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'end_time', 'description')
    search_fields = ('start_time', 'end_time', 'description')


admin.site.register(Forum, ForumAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(ForumProject, ForumProjectAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(EventTime, EventTimeAdmin)
