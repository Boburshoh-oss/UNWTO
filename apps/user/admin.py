from django.contrib import admin
from django.urls import path
from django.http import HttpResponseRedirect
from .models import *


# Register your models here.
class InivitationAdmin(admin.ModelAdmin):
    list_display = ("code", "active")
    list_filter = ("created", "modified")
    search_fields = ("code", )



class UserAdmin(admin.ModelAdmin):
    change_list_template = "entities/excel_button.html"
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
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('mortal/', self.set_download),
        ]
        return my_urls + urls
    
    def set_download(self, request):
        # self.model.objects.all()
        self.message_user(request, "dowloaded users")
        return HttpResponseRedirect("../")

admin.site.register(Inivitation, InivitationAdmin)
admin.site.register(User, UserAdmin)

