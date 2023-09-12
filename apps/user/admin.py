from django.contrib import admin
from django_admin_multi_select_filter.filters import MultiSelectFieldListFilter
from import_export.admin import ExportActionMixin
from .models import *
from .resources import UserResource
from django.utils.translation import gettext_lazy as _

# Register your models here.
class InivitationAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ("code", "active")
    list_filter = ("created", "modified")
    search_fields = ("code",)


class ForumTypeListFilter(admin.SimpleListFilter):
    title = _('Forum Type')
    parameter_name = 'forum_type'

    def lookups(self, request, model_admin):
        data = []
        for user in User.objects.all():
            access_id = user.access_id.split("-")
            serach = access_id[:len(access_id) -1]
            show = "-".join(serach)
            data.append((show, show))
        return data

    def queryset(self, request, queryset):
        if self.value():
            if request.GET.get('forum_type'):
                return queryset.filter(access_id__startswith=self.value())

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
