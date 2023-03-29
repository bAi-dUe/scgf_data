from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import (
    Topic,
    Dynamic,
    Article,
    Comment
)
# Register your models here.


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ["topic", "preview", "followed", "nums", "click_num", "add_time"]
    readonly_fields = ('nums', 'followed',"click_num","add_time")
    search_fields = ("topic",)
    ordering = ("followed", "nums", "click_num")
    list_per_page = 30
    fieldsets = (
        (None, {
            'fields': (
                'topic',
                'image',
                'desc',
                ('click_num', 'followed', "nums"),
                "add_time"
            )
        }),
    )

    def preview(self, obj):
        try:
            img = mark_safe('<img src="%s" width="50px" />' % (obj.image,))
        except Exception as e:
            img = ''
        return img
    preview.short_description = '图片'
    preview.allow_tags = True


@admin.register(Dynamic)
class DynamicAdmin(admin.ModelAdmin):
    list_display = ('text', 'topic', 'user', 'fabulous_num','fav_num','comment_num',"click_num", 'add_time')
    ordering = ("-add_time", 'fabulous_num',"fav_num", "comment_num","click_num")
    list_filter = ('topic',"user")
    raw_id_fields = ("topic", "user")
    list_select_related = ("topic", "user")
    readonly_fields = ("add_time", "click_num","fabulous_num","fav_num","comment_num")
    fieldsets = (
        (None, {
            'fields': (
                'topic',
                "user",
                'text',
                ("click_num","fabulous_num","fav_num","comment_num"),
                "add_time",
            )
        }),
    )


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title',"user", "click_num", "fabulous_num", "fav_num", "comment_num", "add_time")
    ordering = ("-add_time", 'fabulous_num', "fav_num", "comment_num", "click_num")
    list_filter = ("user",)
    raw_id_fields = ("user",)
    list_select_related = ("user",)
    search_fields = ("title",)
    readonly_fields = ("add_time", "click_num","fabulous_num","fav_num","comment_num")
    fieldsets = (
        (None, {
            'fields': (
                'title',
                "user",
                'content',
                ("click_num", "fabulous_num", "fav_num", "comment_num"),
                "add_time",
            )
        }),
    )
    list_per_page = 30


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("content", "user", "content_object", "comment_num", "like", "dislike", "add_time")
    list_filter = ("deleted", )
    raw_id_fields = ("user", )
    list_select_related = ("user",)
    ordering = ("comment_num", "like", "dislike", "add_time")
    readonly_fields = ("add_time", "comment_num", "like", "dislike")
    fieldsets = (
        (None, {
            'fields': (
                'user',
                ("content_type","object_id"),
                'content',
                ("comment_num", "like", "dislike",),
                "add_time",
            )
        }),
    )
    list_per_page = 50

