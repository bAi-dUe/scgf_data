from django.contrib import admin

from .models import (
    Poem,
    Poet,
    MingJu,
    PerfectPoem,
    PerfectPoet,
    AddPoem,
    AddPoet
)
# Register your models here.


@admin.register(Poem)
class PoemAdmin(admin.ModelAdmin):
    list_display = ('title','author', "remark", 'fav_num',"click_num")
    raw_id_fields = ("author",)
    relfield_style = 'fk-ajax'
    list_select_related = ("author",)
    list_filter = ('author__dy',)
    search_fields = ('title',"author__name")
    ordering = ('fav_num', "click_num")
    readonly_fields = ("fav_num", "click_num")
    list_per_page = 50
    fieldsets = (
        (None, {
            "fields": (
                "title",
                "author",
                "remark",
                ("fav_num", "click_num"),
                "content",
                "image",
                "background",
                "appreciation",
                "annotation",
                "translation"
            )
        }),
    )


@admin.register(Poet)
class PoetAdmin(admin.ModelAdmin):
    list_display = ('name', 'other_name', 'dy', 'born', 'death',  'fav_num',"click_num","work_num")
    list_filter = ('dy',)
    search_fields = ('name',)
    ordering = ('fav_num', "click_num", "work_num")
    readonly_fields = ("click_num", "fav_num")
    relfield_style = 'fk-ajax'
    list_per_page = 50
    fieldsets = (
        (None, {
            "fields": (
                ("name","dy"),
                "other_name",
                "image",
                ("born", "death"),
                ("work_num", "fav_num", "click_num"),
                "introduce",
                "lifetime",
                "achievement",
            )
        }),
    )



@admin.register(PerfectPoem)
class PerfectPoemAdmin(admin.ModelAdmin):
    list_display = ('poem', 'user', "tag", 'result', "add_time")
    raw_id_fields = ('poem', 'user')
    list_filter = ('result',)
    list_editable = ('result', )
    ordering = ("-add_time",)
    list_per_page = 30


@admin.register(PerfectPoet)
class PerfectPoetAdmin(admin.ModelAdmin):
    list_display = ('poet', 'user', "other_name", 'result', "add_time")
    raw_id_fields = ('poet', 'user')
    list_filter = ('result',)
    list_editable = ('result',)
    ordering = ("-add_time",)
    list_per_page = 30


@admin.register(AddPoem)
class AddPoemAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', "user","tag", 'result', "add_time")
    raw_id_fields = ('user',)
    list_filter = ('result',)
    list_editable = ('result',)
    ordering = ("-add_time",)
    list_per_page = 30


@admin.register(AddPoet)
class AddPoetAdmin(admin.ModelAdmin):
    list_display = ('name', 'dynasty', "user", "other_name", 'result', "add_time")
    raw_id_fields = ('user',)
    list_filter = ('result','dynasty')
    list_editable = ('result',)
    ordering = ("-add_time",)
    list_per_page = 30


@admin.register(MingJu)
class MingJuAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    search_fields = ('title', 'content')
    raw_id_fields = ("poem",)
    relfield_style = 'fk-ajax'
    list_select_related = ("poem",)
    list_per_page = 50