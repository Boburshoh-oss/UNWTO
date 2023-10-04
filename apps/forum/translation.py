from .models import Forum, Organization, ForumProject, Event, EventTime, MapEventTime, MapEvent, Map
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

class MapTranslationOptions(TranslationOptions):
    fields = ('title',)

translator.register(Map, MapTranslationOptions)

class MapEventTranslationOptions(TranslationOptions):
    fields = ('day', )
    
translator.register(MapEvent, MapEventTranslationOptions)

class MapEventTimeTranslationOptions(TranslationOptions):
    fields = ('description', )

translator.register(MapEventTime, MapEventTimeTranslationOptions)