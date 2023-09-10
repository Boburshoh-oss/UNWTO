from django.contrib import admin
from django_admin_multi_select_filter.filters import MultiSelectFieldListFilter
from import_export.admin import ExportActionMixin
from .models import *
from .resources import UserResource


# Register your models here.
class InivitationAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display = ("code", "active")
    list_filter = ("created", "modified")
    search_fields = ("code", )



class UserAdmin(ExportActionMixin,admin.ModelAdmin):
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
    list_filter = ("created", "modified","organization",("forum_type__title",MultiSelectFieldListFilter),("organization__title",MultiSelectFieldListFilter))
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

