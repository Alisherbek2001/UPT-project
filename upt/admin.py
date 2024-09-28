from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import *


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('fullname_en','fullname_uz','fullname_ru')
    fieldsets = (
        (_('Uzbek'), {'fields': ('fullname_uz', 'position_uz')}),
        (_('English'), {'fields': ('fullname_en', 'position_en')}),
        (_('Russian'), {'fields': ('fullname_ru', 'position_ru')}),
        (_('Photo'),{'fields':('photo',)}),
    )
    

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title_en','title_uz','title_ru')
    fieldsets = (
        (_('Uzbek'), {'fields': ('title_uz',)}),
        (_('English'), {'fields': ('title_en',)}),
        (_('Russian'), {'fields': ('title_ru',)}),
    )

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title_en','title_uz','title_ru')
    fieldsets = (
        (_('Uzbek'), {'fields': ('title_uz',)}),
        (_('English'), {'fields': ('title_en',)}),
        (_('Russian'), {'fields': ('title_ru',)}),
        (_('Photo'), {'fields': ('photo',)}),
        (_('Category'),{'fields': ('category',)}),
        (_('Link'), {'fields': ('link',)}),
        (_('Is Main'), {'fields': ('is_main',)}),
    )


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('author_en','author_uz','author_ru')
    fieldsets = (
        (_('Uzbek'), {'fields': ('text_uz','author_uz')}),
        (_('English'), {'fields': ('text_en','author_en')}),
        (_('Russian'), {'fields': ('text_ru','author_ru')}),
    )