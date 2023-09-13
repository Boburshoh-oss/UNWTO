from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import *
from openpyxl import Workbook, styles
from openpyxl.drawing.image import Image
from django.http import HttpResponse
from django.utils.safestring import mark_safe
from openpyxl import Workbook
from ckeditor.widgets import CKEditorWidget

# Forum admin
class EventTabularInline(admin.TabularInline):
    model = Event
    extra = 0


@admin.register(Forum)
class ForumAdmin(TranslationAdmin):
    list_display = ("title", "short_key", "description", "created", "modified")
    list_filter = ("created", "modified")
    search_fields = ("title", "description", "organization__title")
    inlines = [EventTabularInline]
    actions = ["export_selected_to_excel"]
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget()},
    }
    def image_tag(self, obj):
        if obj.image:
            return mark_safe('<img src="{}" width="50" height="50" />'.format(obj.image.url))
        return "-"

    image_tag.short_description = "Image"

    def export_selected_to_excel(self, request, queryset):

        # Create a new workbook and add a worksheet
        workbook = Workbook()
        worksheet = workbook.active

        # Add headers to the Excel file
        worksheet.append(["Title", "Short_key", "Organization", "Description"])

        # Loop through the selected objects and add rows to the Excel file
        image_style = styles.Font(size=60)

        border = styles.Border(left=styles.Side(border_style=None,
                                                color='FF000000'),
                               right=styles.Side(border_style=None,
                                                 color='FF000000'),
                               top=styles.Side(border_style=None,
                                               color='FF000000'),
                               bottom=styles.Side(border_style=None,
                                                  color='FF000000'),
                               diagonal=styles.Side(border_style=None,
                                                    color='FF000000'),
                               diagonal_direction=0,
                               outline=styles.Side(border_style=None,
                                                   color='FF000000'),
                               vertical=styles.Side(border_style=None,
                                                    color='FF000000'),
                               horizontal=styles.Side(border_style=None,
                                                      color='FF000000')
                               )
        alignment = styles.Alignment(horizontal='general',
                                     vertical='bottom',
                                     text_rotation=0,
                                     wrap_text=False,
                                     shrink_to_fit=False,
                                     indent=0)
        protection = styles.Protection(locked=True,
                                       hidden=False)
        s = 2
        for project in queryset:
            worksheet.append([project.title, project.subtitle, project.context, " "])

            # Add the image to the Excel file
            if project.image:
                img = Image(project.image.path)
                img.width = 100  # Adjust the image size as needed
                img.height = 100
                worksheet.add_image(img, "D{}".format(worksheet.max_row))  # Add image to column D
                work_image = worksheet["D" + str(s)]
                work_image.font = image_style
            work_desc = worksheet["C" + str(s)]
            s += 1
            work_desc.alignment = alignment
            work_desc.border = border

        # Create an HTTP response with the Excel file
        response = HttpResponse(content_type="application/ms-excel")
        response["Content-Disposition"] = "attachment; filename=forum_projects.xlsx"

        # Save the workbook to the response
        workbook.save(response)

        return response


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("title", "created", "modified")
    list_filter = ("created", "modified")
    search_fields = ("title",)
    actions = ["export_selected_to_excel"]

    def image_tag(self, obj):
        if obj.image:
            return mark_safe('<img src="{}" width="50" height="50" />'.format(obj.image.url))
        return "-"

    image_tag.short_description = "Image"

    def export_selected_to_excel(self, request, queryset):

        # Create a new workbook and add a worksheet
        workbook = Workbook()
        worksheet = workbook.active

        # Add headers to the Excel file
        worksheet.append(["Title"])

        # Loop through the selected objects and add rows to the Excel file
        image_style = styles.Font(size=60)

        border = styles.Border(left=styles.Side(border_style=None,
                                                color='FF000000'),
                               right=styles.Side(border_style=None,
                                                 color='FF000000'),
                               top=styles.Side(border_style=None,
                                               color='FF000000'),
                               bottom=styles.Side(border_style=None,
                                                  color='FF000000'),
                               diagonal=styles.Side(border_style=None,
                                                    color='FF000000'),
                               diagonal_direction=0,
                               outline=styles.Side(border_style=None,
                                                   color='FF000000'),
                               vertical=styles.Side(border_style=None,
                                                    color='FF000000'),
                               horizontal=styles.Side(border_style=None,
                                                      color='FF000000')
                               )
        alignment = styles.Alignment(horizontal='general',
                                     vertical='bottom',
                                     text_rotation=0,
                                     wrap_text=False,
                                     shrink_to_fit=False,
                                     indent=0)
        protection = styles.Protection(locked=True,
                                       hidden=False)
        s = 2
        for project in queryset:
            worksheet.append([project.title, project.subtitle, project.context, " "])

            # Add the image to the Excel file
            if project.image:
                img = Image(project.image.path)
                img.width = 100  # Adjust the image size as needed
                img.height = 100
                worksheet.add_image(img, "D{}".format(worksheet.max_row))  # Add image to column D
                work_image = worksheet["D" + str(s)]
                work_image.font = image_style
            work_desc = worksheet["C" + str(s)]
            s += 1
            work_desc.alignment = alignment
            work_desc.border = border

        # Create an HTTP response with the Excel file
        response = HttpResponse(content_type="application/ms-excel")
        response["Content-Disposition"] = "attachment; filename=forum_projects.xlsx"

        # Save the workbook to the response
        workbook.save(response)

        return response


class ForumProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "subtitle", "context", "created", "modified")
    list_filter = ("created", "modified")
    search_fields = ("title", "subtitle", "context")
    actions = ["export_selected_to_excel"]

    def export_selected_to_excel(self, request, queryset):

        # Create a new workbook and add a worksheet
        workbook = Workbook()
        worksheet = workbook.active

        # Add headers to the Excel file
        worksheet.append(["Forum", "Title", "Subtitle", "Context", "Image", ])

        # Loop through the selected objects and add rows to the Excel file
        image_style = styles.Font(size=60)

        border = styles.Border(left=styles.Side(border_style=None,
                                                color='FF000000'),
                               right=styles.Side(border_style=None,
                                                 color='FF000000'),
                               top=styles.Side(border_style=None,
                                               color='FF000000'),
                               bottom=styles.Side(border_style=None,
                                                  color='FF000000'),
                               diagonal=styles.Side(border_style=None,
                                                    color='FF000000'),
                               diagonal_direction=0,
                               outline=styles.Side(border_style=None,
                                                   color='FF000000'),
                               vertical=styles.Side(border_style=None,
                                                    color='FF000000'),
                               horizontal=styles.Side(border_style=None,
                                                      color='FF000000')
                               )
        alignment = styles.Alignment(horizontal='general',
                                     vertical='bottom',
                                     text_rotation=0,
                                     wrap_text=False,
                                     shrink_to_fit=False,
                                     indent=0)
        protection = styles.Protection(locked=True,
                                       hidden=False)
        s = 2
        for project in queryset:
            worksheet.append([project.title, project.subtitle, project.context, " "])

            # Add the image to the Excel file
            if project.image:
                img = Image(project.image.path)
                img.width = 100  # Adjust the image size as needed
                img.height = 100
                worksheet.add_image(img, "D{}".format(worksheet.max_row))  # Add image to column D
                work_image = worksheet["E" + str(s)]
                work_image.font = image_style
            work_desc = worksheet["C" + str(s)]
            s += 1
            work_desc.alignment = alignment
            work_desc.border = border

        # Create an HTTP response with the Excel file
        response = HttpResponse(content_type="application/ms-excel")
        response["Content-Disposition"] = "attachment; filename=forum_projects.xlsx"

        # Save the workbook to the response
        workbook.save(response)

        return response


class EventTimeAdmin(admin.ModelAdmin):
    list_display = ("start_time", "end_time", "description")
    search_fields = ("start_time", "end_time", "description")
    actions = ["export_selected_to_excel"]

    def export_selected_to_excel(self, request, queryset):

        # Create a new workbook and add a worksheet
        workbook = Workbook()
        worksheet = workbook.active

        # Add headers to the Excel file
        worksheet.append(["Start_time", "End_time", 'Description', 'Event'])

        # Loop through the selected objects and add rows to the Excel file
        image_style = styles.Font(size=60)

        border = styles.Border(left=styles.Side(border_style=None,
                                                color='FF000000'),
                               right=styles.Side(border_style=None,
                                                 color='FF000000'),
                               top=styles.Side(border_style=None,
                                               color='FF000000'),
                               bottom=styles.Side(border_style=None,
                                                  color='FF000000'),
                               diagonal=styles.Side(border_style=None,
                                                    color='FF000000'),
                               diagonal_direction=0,
                               outline=styles.Side(border_style=None,
                                                   color='FF000000'),
                               vertical=styles.Side(border_style=None,
                                                    color='FF000000'),
                               horizontal=styles.Side(border_style=None,
                                                      color='FF000000')
                               )
        alignment = styles.Alignment(horizontal='general',
                                     vertical='bottom',
                                     text_rotation=0,
                                     wrap_text=False,
                                     shrink_to_fit=False,
                                     indent=0)
        protection = styles.Protection(locked=True,
                                       hidden=False)
        s = 2
        for project in queryset:
            worksheet.append([project.title, project.subtitle, project.context, " "])

            # Add the image to the Excel file
            if project.image:
                img = Image(project.image.path)
                img.width = 100  # Adjust the image size as needed
                img.height = 100
                worksheet.add_image(img, "D{}".format(worksheet.max_row))  # Add image to column D
                work_image = worksheet["D" + str(s)]
                work_image.font = image_style
            work_desc = worksheet["C" + str(s)]
            s += 1
            work_desc.alignment = alignment
            work_desc.border = border

        # Create an HTTP response with the Excel file
        response = HttpResponse(content_type="application/ms-excel")
        response["Content-Disposition"] = "attachment; filename=forum_projects.xlsx"

        # Save the workbook to the response
        workbook.save(response)

        return response


class EventTimeTabularInline(admin.TabularInline):
    model = EventTime
    extra = 0


class EventAdmin(admin.ModelAdmin):
    list_display = ("day", "forum", "date", "created", "modified")
    list_filter = ("created", "modified", "forum")
    search_fields = ("day", "date")
    inlines = [EventTimeTabularInline]
    actions = ["export_selected_to_excel"]

    def image_tag(self, obj):
        if obj.image:
            return mark_safe('<img src="{}" width="50" height="50" />'.format(obj.image.url))
        return "-"

    image_tag.short_description = "Image"

    def export_selected_to_excel(self, request, queryset):

        # Create a new workbook and add a worksheet
        workbook = Workbook()
        worksheet = workbook.active

        # Add headers to the Excel file
        worksheet.append(["Day", "Date", "Forum"])

        # Loop through the selected objects and add rows to the Excel file
        image_style = styles.Font(size=60)

        border = styles.Border(left=styles.Side(border_style=None,
                                                color='FF000000'),
                               right=styles.Side(border_style=None,
                                                 color='FF000000'),
                               top=styles.Side(border_style=None,
                                               color='FF000000'),
                               bottom=styles.Side(border_style=None,
                                                  color='FF000000'),
                               diagonal=styles.Side(border_style=None,
                                                    color='FF000000'),
                               diagonal_direction=0,
                               outline=styles.Side(border_style=None,
                                                   color='FF000000'),
                               vertical=styles.Side(border_style=None,
                                                    color='FF000000'),
                               horizontal=styles.Side(border_style=None,
                                                      color='FF000000')
                               )
        alignment = styles.Alignment(horizontal='general',
                                     vertical='bottom',
                                     text_rotation=0,
                                     wrap_text=False,
                                     shrink_to_fit=False,
                                     indent=0)
        protection = styles.Protection(locked=True,
                                       hidden=False)
        s = 2
        for project in queryset:
            worksheet.append([project.title, project.subtitle, project.context, " "])

            # Add the image to the Excel file
            if project.image:
                img = Image(project.image.path)
                img.width = 100  # Adjust the image size as needed
                img.height = 100
                worksheet.add_image(img, "D{}".format(worksheet.max_row))  # Add image to column D
                work_image = worksheet["D" + str(s)]
                work_image.font = image_style
            work_desc = worksheet["C" + str(s)]
            s += 1
            work_desc.alignment = alignment
            work_desc.border = border

        # Create an HTTP response with the Excel file
        response = HttpResponse(content_type="application/ms-excel")
        response["Content-Disposition"] = "attachment; filename=forum_projects.xlsx"

        # Save the workbook to the response
        workbook.save(response)

        return response


# admin.site.register(Forum, ForumAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(ForumProject, ForumProjectAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(EventTime, EventTimeAdmin)
