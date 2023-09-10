from django.contrib import admin
from django.urls import path
from django.http import HttpResponseRedirect, HttpResponse
import csv
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
            path('export_csv/', self.export_csv),
        ]
        return my_urls + urls

    def export_csv(self, request):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in self.model.objects.all():
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

admin.site.register(Inivitation, InivitationAdmin)
admin.site.register(User, UserAdmin)

