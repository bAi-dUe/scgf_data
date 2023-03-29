import xadmin
from xadmin.layout import Fieldset, Main, Row

from .models import (
    Article,
    Dynamic,
    Topic,
    Comment
)


class TopicAdmin:
    fields = ["topic", "image", "desc","click_num", "followed", "nums", "add_time"]
    list_display = ["topic", "followed", "nums", "click_num", "add_time"]
    readonly_fields = ('nums', 'followed', "click_num", "add_time")
    search_fields = ("topic",)
    ordering = ("-add_time","followed", "nums", "click_num")
    list_per_page = 30
    relfield_style = 'fk-ajax'
    model_icon = "fa fa-twitter"

    def get_form_layout(self):
        if self.org_obj:
            self.form_layout = (
                Main(
                    Fieldset('',
                             Row('topic'),
                             Row('followed', 'nums',"click_num"),
                             Row('image'),
                             Row('add_time')
                             ),
                ),
            )
        return super().get_form_layout()


class DynamicAdmin:
    fields = ("text", "topic","user","text","click_num","fabulous_num","fav_num","comment_num", "deleted", "add_time")
    list_display = ('text', 'topic', 'user', 'fabulous_num', 'fav_num', 'comment_num', "click_num", 'add_time', "deleted")
    ordering = ("-add_time", 'fabulous_num', "fav_num", "comment_num", "click_num")
    list_filter = ('topic', "user")
    list_editable = ("deleted",)
    raw_id_fields = ("topic","user")
    list_select_related = ("topic","user")
    readonly_fields = ("add_time", "click_num", "fabulous_num", "fav_num", "comment_num")
    list_per_page = 30
    relfield_style = 'fk-ajax'
    model_icon = "fa fa-spinner fa-pulse fa-fw margin-bottom"

    def get_form_layout(self):
        if self.org_obj:
            self.form_layout = (
                Main(
                    Fieldset('',
                             Row('topic'),
                             Row('user'),
                             Row('fabulous_num', 'fav_num', 'comment_num',"click_num"),
                             Row("add_time"),
                             Row("deleted")
                             ),
                    Fieldset('',
                             Row('text'),
                             ),
                ),
            )
        return super().get_form_layout()


class ArticleAdmin:
    fields = ("title", "user", "content", "click_num", "fabulous_num","fav_num","comment_num", "deleted", "add_time")
    list_display = ('title', "user", "click_num", "fabulous_num", "fav_num", "comment_num", "add_time", "deleted")
    ordering = ("-add_time", 'fabulous_num', "fav_num", "comment_num", "click_num")
    list_filter = ("user",)
    raw_id_fields = ("user",)
    list_editable = ("deleted",)
    list_select_related = ("user",)
    search_fields = ("title",)
    readonly_fields = ("add_time", "click_num", "fabulous_num", "fav_num", "comment_num")
    list_per_page = 30
    relfield_style = 'fk-ajax'
    model_icon = "fa fa-file-text"

    def get_form_layout(self):
        if self.org_obj:
            self.form_layout = (
                Main(
                    Fieldset('',
                             Row('title'),
                             Row('user'),
                             Row('fav_num', 'comment_num', "click_num", "fabulous_num"),
                             Row("add_time"),
                             Row("deleted")
                             ),
                    Fieldset('',
                             Row('content'),
                             ),
                ),
            )
        return super().get_form_layout()


class CommentAdmin:
    fields = ("user", "like", "dislike", "add_time", "content", "comment_num", "deleted", )
    list_display = ('content', "user", "like", "dislike", "comment_num", "add_time", "deleted")
    ordering = ("-add_time", 'like', "dislike", "comment_num",)
    list_filter = ("user",)
    raw_id_fields = ("user",)
    list_editable = ("deleted",)
    list_select_related = ("user",)
    readonly_fields = ("add_time", "like", "dislike", "comment_num", "add_time")
    list_per_page = 30
    relfield_style = 'fk-ajax'
    model_icon = "fa fa-file-text"

    def get_form_layout(self):
        if self.org_obj:
            self.form_layout = (
                Main(
                    Fieldset('',
                             Row('content'),
                             Row('user'),
                             Row('like', 'dislike', "comment_num"),
                             Row("add_time"),
                             Row("deleted")
                             ),
                ),
            )
        return super().get_form_layout()


xadmin.site.register(Topic, TopicAdmin)
xadmin.site.register(Dynamic, DynamicAdmin)
xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(Comment, CommentAdmin)