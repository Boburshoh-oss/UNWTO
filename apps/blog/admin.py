from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from import_export.admin import ExportActionMixin
from .models import *

# Register your models here.
admin.site.register(SocialMedia)
admin.site.register(Banner)

@admin.register(Contact)
class ForumAdmin(ExportActionMixin):
    list_display = ("name",
    search_fields = ("name",)

    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget()},
    }
