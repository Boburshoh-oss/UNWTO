from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Forum)
admin.site.register(ForumProject)
admin.site.register(Organization)
admin.site.register(Event)
admin.site.register(EventTime)
