from django.contrib import admin
from django_admin_multi_select_filter.filters import MultiSelectFieldListFilter
from import_export.admin import ExportActionMixin
from .models import *
from .resources import UserResource


# Register your models here.
class InivitationAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ("code", "active")
    list_filter = ("created", "modified")
    search_fields = ("code",)


from django.contrib.admin import SimpleListFilter


class ForumTypeListFilter(SimpleListFilter):
    title = 'Forum Type'
    parameter_name = 'forum_type'

    def lookups(self, request, model_admin):
        return [(str(forum.id), forum.title) for forum in Forum.objects.all()]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(forum_type__id=self.value())


class UserAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = UserResource

    list_display = (
        "first_name",
        "last_name",
        "date_of_birth",
        "country",
        "expire_date",
        "organization",
        "access_id",
        "invitation_id",
    )
    list_filter = (
        "created",
        "modified",
        "organization",
        ForumTypeListFilter,
    )
    search_fields = (
        "first_name",
        "last_name",
        "country",
        "organization",
        "access_id",
        "invitation_id",
    )


admin.site.register(Inivitation, InivitationAdmin)
admin.site.register(User, UserAdmin)
