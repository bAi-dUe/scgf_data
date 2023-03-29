import xadmin

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



class CollectPoemAdmin:
    list_display = ['user', 'poem', 'add_time']
    raw_id_fields = ("user","poem")
    relfield_style = 'fk-ajax'
    list_per_page = 50


class CollectPoetAdmin:
    list_display = ['user', 'poet', 'add_time']
    raw_id_fields = ("user","poet")
    relfield_style = 'fk-ajax'
    list_per_page = 50


class CollectDynamicAdmin:
    list_display = ['user', 'dynamic', 'add_time']
    raw_id_fields = ("user","dynamic")
    relfield_style = 'fk-ajax'
    list_per_page = 50


class CollectArticleAdmin:
    list_display = ['user', 'article', 'add_time']
    raw_id_fields = ("user","article")
    relfield_style = 'fk-ajax'
    list_per_page = 50


class FabulousDynamicAdmin:
    list_display = ['user', 'dynamic', 'add_time']
    raw_id_fields = ("user","dynamic")
    relfield_style = 'fk-ajax'
    list_per_page = 50


class FabulousArticleAdmin:
    list_display = ['user', 'article', 'add_time']
    raw_id_fields = ("user","article")
    relfield_style = 'fk-ajax'
    list_per_page = 50


class FollowTopicAdmin:
    list_display = ['user', 'topic', 'add_time']
    raw_id_fields = ("user","topic")
    relfield_style = 'fk-ajax'
    list_per_page = 50


class FollowUserAdmin:
    list_display = ['user', 'followed_user', 'add_time']
    raw_id_fields = ("user","followed_user")
    relfield_style = 'fk-ajax'
    list_per_page = 50


class LikeCommentAdmin:
    list_display = ['user', 'comment', 'add_time']
    raw_id_fields = ("user","comment")
    relfield_style = 'fk-ajax'
    list_per_page = 50


class DislikeCommentAdmin:
    list_display = ['user', 'comment', 'add_time']
    raw_id_fields = ("user","comment")
    relfield_style = 'fk-ajax'
    list_per_page = 50


xadmin.site.register(CollectPoem, CollectPoemAdmin)
xadmin.site.register(CollectPoet, CollectPoetAdmin)
xadmin.site.register(CollectArticle, CollectArticleAdmin)
xadmin.site.register(CollectDynamic, CollectDynamicAdmin)
xadmin.site.register(FabulousDynamic, FabulousDynamicAdmin)
xadmin.site.register(FabulousArticle, FabulousArticleAdmin)
xadmin.site.register(FollowTopic, FollowTopicAdmin)
xadmin.site.register(FollowUser, FollowUserAdmin)
xadmin.site.register(LikeComment, LikeCommentAdmin)
xadmin.site.register(DislikeComment, DislikeCommentAdmin)
