from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import *
from openpyxl import Workbook, styles
from openpyxl.drawing.image import Image
from django.http import HttpResponse
from django.utils.safestring import mark_safe
from openpyxl import Workbook
from import_export.admin import ExportActionMixin
from ckeditor.widgets import CKEditorWidget

# Forum admin
class EventTabularInline(admin.TabularInline):
    model = Event
    extra = 0


@admin.register(Forum)
class ForumAdmin(ExportActionMixin,TranslationAdmin):
    list_display = ("title", "short_key", "description", "created", "modified")
    list_filter = ("created", "modified")
    search_fields = ("title", "description", "organization__title")
    inlines = [EventTabularInline]

    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget()},
    }





class OrganizationAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display = ("title", "created", "modified")
    list_filter = ("created", "modified")
    search_fields = ("title",)


class ForumProjectAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display = ("title", "subtitle", "context", "created", "modified")
    list_filter = ("created", "modified")
    search_fields = ("title", "subtitle", "context")
    
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget()},
    }

class EventTimeAdmin(admin.ModelAdmin):
    list_display = ("start_time", "end_time", "description")
    search_fields = ("start_time", "end_time", "description")
  


class EventTimeTabularInline(admin.TabularInline):
    model = EventTime
    extra = 0


class EventAdmin(admin.ModelAdmin):
    list_display = ("day", "forum", "date", "created", "modified")
    list_filter = ("created", "modified", "forum")
    search_fields = ("day", "date")
    inlines = [EventTimeTabularInline]


# Forum admin
class MapEventTabularInline(admin.TabularInline):
    model = MapEvent
    extra = 0


@admin.register(Map)
class MapAdmin(TranslationAdmin):
    list_display = ("title","created", "modified")
    list_filter = ("created", "modified")
    inlines = [MapEventTabularInline]


class MapEventTimeAdmin(admin.ModelAdmin):
    list_display = ("start_time", "end_time", "description")
    search_fields = ("start_time", "end_time", "description")
  


class MapEventTimeTabularInline(admin.TabularInline):
    model = MapEventTime
    extra = 0


class MapEventAdmin(admin.ModelAdmin):
    list_display = ("day", "map", "date", "created", "modified")
    list_filter = ("created", "modified", "map")
    search_fields = ("day", "date")
    inlines = [MapEventTimeTabularInline]


# admin.site.register(Forum, ForumAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(ForumProject, ForumProjectAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(EventTime, EventTimeAdmin)
admin.site.register(MapEvent, MapEventAdmin)
admin.site.register(MapEventTime, MapEventTimeAdmin)