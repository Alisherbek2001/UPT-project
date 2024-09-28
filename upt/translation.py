from modeltranslation.translator import register,TranslationOptions
from .models import *


@register(Member)
class MemberTranslateOption(TranslationOptions):
    fields = ('fullname','position')


@register(Category)
class CategoryTranslateOption(TranslationOptions):
    fields = ('title',)


@register(Project)
class ProjectTranslateOption(TranslationOptions):
    fields = ('title',)
    

@register(Feedback)
class FeedbackTranslateOption(TranslationOptions):
    fields = ('text','author')