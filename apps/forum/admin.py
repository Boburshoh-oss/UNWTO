from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from import_export.admin import ExportActionMixin
from .models import *


# Forum admin
class EventTabularInline(admin.TabularInline):
    model = Event
    extra = 0

@admin.register(Forum)
class ForumAdmin(ExportActionMixin, TranslationAdmin):
    list_display = ("title","short_key", "description", "created", "modified")
    list_filter = ("created", "modified")
    search_fields = ("title", "description", "organization__title")
    inlines = [EventTabularInline]

class OrganizationAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ("title", "created", "modified")
    list_filter = ("created", "modified")
    search_fields = ("title",)


class ForumProjectAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ("title", "subtitle", "context", "created", "modified")
    list_filter = ("created", "modified")
    search_fields = ("title", "subtitle", "context")


class EventTimeAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ("start_time", "end_time", "description")
    search_fields = ("start_time", "end_time", "description")


class EventTimeTabularInline(admin.TabularInline):
    model = EventTime
    extra = 0


class EventAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ("day","forum", "date", "created", "modified")
    list_filter = ("created", "modified","forum")
    search_fields = ("day", "date")
    inlines = [EventTimeTabularInline]


# admin.site.register(Forum, ForumAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(ForumProject, ForumProjectAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(EventTime, EventTimeAdmin)
