from modeltranslation.translator import register, TranslationOptions
from .models import Contact

@register(Contact)
class ContactTranslationOptions(TranslationOptions):
    fields = ('title',)  # specify the fields you want to translate
