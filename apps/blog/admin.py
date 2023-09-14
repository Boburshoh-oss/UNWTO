from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from import_export.admin import ExportActionMixin
from modeltranslation.admin import TranslationAdmin

from .models import *

# Register your models here.
admin.site.register(SocialMedia)
admin.site.register(Banner)



@admin.register(Connect)
class ConnectAdmin(TranslationAdmin, admin.ModelAdmin):
    list_display = ("type","title","name","active")
    search_fields = ("name","title")
    list_filter = ("active","type")