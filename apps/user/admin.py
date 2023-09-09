from django.contrib import admin

from .models import *


# Register your models here.
class InivitationAdmin(admin.ModelAdmin):
    list_display = ("code", "active")
    list_filter = ("created", "modified")
    search_fields = ("code", )


class UserAdmin(admin.ModelAdmin):
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
    list_filter = ("created", "modified")
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
