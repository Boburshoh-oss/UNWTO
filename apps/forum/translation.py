from .models import Forum, Organization, ForumProject, Event, EventTime
from modeltranslation.translator import translator, TranslationOptions

class ForumTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
translator.register(Forum, ForumTranslationOptions)

class OrgTranslationOptions(TranslationOptions):
    fields = ('title', )
    
translator.register(Organization, OrgTranslationOptions)

class ForumProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'context')
    
translator.register(ForumProject, ForumProjectTranslationOptions)

class EventTranslationOptions(TranslationOptions):
    fields = ('day', )
    
translator.register(Event, EventTranslationOptions)

class EventTimeTranslationOptions(TranslationOptions):
    fields = ('description', )
    
translator.register(EventTime, EventTimeTranslationOptions)