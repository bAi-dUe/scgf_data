from django.contrib import admin

from .models import (
    PoemCompletion,
    PoemGenerate
)
# Register your models here.


@admin.register(PoemCompletion)
class PoemCompletionAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'other1', 'other2', 'other3')
    search_fields = ('question', )
    list_per_page = 50


@admin.register(PoemGenerate)
class PoemGenerateAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    search_fields = ('title',)
    list_per_page = 50