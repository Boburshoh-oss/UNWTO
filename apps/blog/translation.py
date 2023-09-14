from modeltranslation.translator import register, TranslationOptions
from .models import  Connect



@register(Connect)
class ConnectTranslationOptions(TranslationOptions):
    fields = ('title',)  # specify the fields you want to translate