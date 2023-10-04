import os
from django.contrib import admin
from import_export.admin import ExportActionMixin
from .models import *
from .resources import UserResource
import pycountry
from openpyxl import Workbook, styles
from openpyxl.drawing.image import Image
from PIL import Image as PILImage
from django.http import HttpResponse
from openpyxl import Workbook
from django.urls import path
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from .utils import convert_to_jpeg

# Register your models here.
class InivitationAdmin(ExportActionMixin, admin.ModelAdmin):
    change_list_template="entities/invitation_redirect.html"
    list_display = ("code", "amount", "active")
    list_filter = ("created", "modified")
    search_fields = ("code",)

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path("generate/", self.invitaion_generate),
        ]
        return my_urls + urls

    def invitaion_generate(self, request):
        # self.message_user(request, "message")
        return render(request, 'entities/index.html')



class ForumTypeListFilter(admin.SimpleListFilter):
    title = _("Forum Type")
    parameter_name = "forum_type"

    def lookups(self, request, model_admin):
        data = []
        for user in User.objects.all():
            access_id = user.access_id.split("-")
            get_short_key = access_id[: len(access_id) - 1]
            show = "-".join(get_short_key)
            data.append((show, show))
        return set(data)

    def queryset(self, request, queryset):
        if self.value():
            if request.GET.get("forum_type"):
                return queryset.filter(access_id__startswith=self.value())

            return queryset.filter(forum_type__id=self.value())


class UserAdmin(admin.ModelAdmin):
    resource_class = UserResource

    list_display = (
        "first_name",
        "last_name",
        "date_of_birth",
        "country",
        "position",
        "expire_date",
        "organization",
        "access_id",
        "invitation_id",
        "phone_number",
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
        "organization__title",
        "access_id",
        "invitation_id__code",
        "phone_number"
    )
    actions = ["export_selected_to_excel"]

    def export_selected_to_excel(self, request, queryset):
        # Create a new workbook and add a worksheet
        workbook = Workbook()
        worksheet = workbook.active

        # Add headers to the Excel file
        worksheet.append(
            [
                "Ismi",
                "Familya",
                "Tug'ulgan kuni",
                "Davlati",
                "Email",
                "Passport",
                "Passport amal qilish muddati",
                "Telfon raqam",
                "Tashkilot",
                "Tashkilot nomi",
                "Lavozimi",
                "Kirish ID",
                "Taklifnoma ID",
                "Rasmi",
                " ",
            ]
        )

        # Loop through the selected objects and add rows to the Excel file
        image_style = styles.Font(size=60)

        border = styles.Border(
            left=styles.Side(border_style=None, color="FF000000"),
            right=styles.Side(border_style=None, color="FF000000"),
            top=styles.Side(border_style=None, color="FF000000"),
            bottom=styles.Side(border_style=None, color="FF000000"),
            diagonal=styles.Side(border_style=None, color="FF000000"),
            diagonal_direction=0,
            outline=styles.Side(border_style=None, color="FF000000"),
            vertical=styles.Side(border_style=None, color="FF000000"),
            horizontal=styles.Side(border_style=None, color="FF000000"),
        )
        alignment = styles.Alignment(
            horizontal="general",
            vertical="bottom",
            text_rotation=0,
            wrap_text=False,
            shrink_to_fit=False,
            indent=0,
        )
        protection = styles.Protection(locked=True, hidden=False)
        s = 2
        for project in queryset:
            worksheet.append(
                [
                    project.first_name,
                    project.last_name,
                    project.date_of_birth,
                    " ",
                    project.email,
                    project.passport,
                    project.expire_date,
                    project.phone_number,
                    project.organization.title,
                    project.org_name,
                    project.position,
                    project.access_id,
                    project.invitation_id.code,
                    " ",
                ]
            )

            # Add the image to the Excel file
            if project.image:
                image_path = project.image.path
                # new_image_path = convert_to_jpeg(image_path)  # Convert to JPEG if it's MPO
                img = Image(image_path) 

                if img.format == "mpo":
                    with PILImage.open(image_path) as img:
                        jpeg_path = os.path.splitext(image_path)[0] + ".jpeg"
                        img.convert("RGB").save(jpeg_path, "JPEG")
                        img = Image(jpeg_path) 

                img.width = 100  # Adjust the image size as needed
                img.height = 100
                worksheet.add_image(
                    img, "N{}".format(worksheet.max_row)
                )  # Add image to column D
                work_image = worksheet["N" + str(s)]

                work_image.font = image_style
            worksheet["C" + str(s)] = project.date_of_birth
            country = str(project.country)
            worksheet["D" + str(s)] = pycountry.countries.get(
                alpha_2=country.lower()
            ).name

            work_desc = worksheet["J" + str(s)]
            s += 1
            work_desc.alignment = alignment
            work_desc.border = border

        # Create an HTTP response with the Excel file
        response = HttpResponse(content_type="application/ms-excel")
        response["Content-Disposition"] = "attachment; filename=forum_projects.xlsx"

        # Save the workbook to the response
        workbook.save(response)

        return response


admin.site.register(Inivitation, InivitationAdmin)
admin.site.register(User, UserAdmin)
