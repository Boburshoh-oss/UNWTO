from modeltranslation.translator import register, TranslationOptions
from .models import Contact, Connect

@register(Contact)
class ContactTranslationOptions(TranslationOptions):
    fields = ('title',)  # specify the fields you want to translate

@register(Connect)
class ConnectTranslationOptions(TranslationOptions):
    fields = ('title',)  # specify the fields you want to translate