from django.contrib import admin

from .models import (
    CollectPoem,
    CollectPoet,
    CollectDynamic,
    CollectArticle,
    FabulousDynamic,
    FabulousArticle,
    FollowTopic,
    FollowUser,
    LikeComment,
    DislikeComment
)


@admin.register(CollectPoem)
class CollectPoemAdmin(admin.ModelAdmin):
    list_display = ['user', 'poem', 'add_time']
    raw_id_fields = ("user","poem")
    relfield_style = 'fk-ajax'
    list_per_page = 50


@admin.register(CollectPoet)
class CollectPoetAdmin(admin.ModelAdmin):
    list_display = ['user', 'poet', 'add_time']
    raw_id_fields = ("user","poet")
    relfield_style = 'fk-ajax'
    list_per_page = 50


@admin.register(CollectDynamic)
class CollectDynamicAdmin(admin.ModelAdmin):
    list_display = ['user', 'dynamic', 'add_time']
    raw_id_fields = ("user","dynamic")
    relfield_style = 'fk-ajax'
    list_per_page = 50


@admin.register(CollectArticle)
class CollectArticleAdmin(admin.ModelAdmin):
    list_display = ['user', 'article', 'add_time']
    raw_id_fields = ("user","article")
    relfield_style = 'fk-ajax'
    list_per_page = 50


@admin.register(FabulousDynamic)
class FabulousDynamicAdmin(admin.ModelAdmin):
    list_display = ['user', 'dynamic', 'add_time']
    raw_id_fields = ("user","dynamic")
    relfield_style = 'fk-ajax'
    list_per_page = 50


@admin.register(FabulousArticle)
class FabulousArticleAdmin(admin.ModelAdmin):
    list_display = ['user', 'article', 'add_time']
    raw_id_fields = ("user","article")
    relfield_style = 'fk-ajax'
    list_per_page = 50


@admin.register(FollowTopic)
class FollowTopicAdmin(admin.ModelAdmin):
    list_display = ['user', 'topic', 'add_time']
    raw_id_fields = ("user","topic")
    relfield_style = 'fk-ajax'
    list_per_page = 50


@admin.register(FollowUser)
class FollowUserAdmin(admin.ModelAdmin):
    list_display = ['user', 'followed_user', 'add_time']
    raw_id_fields = ("user","followed_user")
    relfield_style = 'fk-ajax'
    list_per_page = 50


@admin.register(LikeComment)
class LikeCommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'comment', 'add_time']
    raw_id_fields = ("user","comment")
    relfield_style = 'fk-ajax'
    list_per_page = 50


@admin.register(DislikeComment)
class DislikeCommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'comment', 'add_time']
    raw_id_fields = ("user","comment")
    relfield_style = 'fk-ajax'
    list_per_page = 50