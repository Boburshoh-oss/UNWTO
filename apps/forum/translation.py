from .models import Forum, Organization, ForumProject, Event, EventTime
from modeltranslation.translator import translator, TranslationOptions

class ForumTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
    
translator.register(Forum, ForumTranslationOptions)