import xadmin
from xadmin.layout import Fieldset, Main, Side, Row

from .models import (
    Poet,
    Poem,
    MingJu,
    PerfectPoem,
    PerfectPoet,
    AddPoem,
    AddPoet,
    TaggedItem,
)


class TagAdmin:
    list_display = ('tag', 'content_type', 'object_id','obj')


class MingJuAdmin:
    list_display = ('content', 'title', 'author')
    search_fields = ('content', 'title')
    raw_id_fields = ("poem",)
    list_select_related = ("poem",)
    show_detail_fields = ("poem",)
    # readonly_fields = ("poem", )
    relfield_style = 'fk-ajax'
    list_per_page = 50
    model_icon = "fa fa-star"

    def get_form_layout(self):
        if self.org_obj:
            self.form_layout = (
                Main(
                    Fieldset('',
                             Row('poem'),
                             Row('title'),
                             Row('content'),
                             ),
                ),
            )
        return super().get_form_layout()


class PoemAdmin:
    fields = ("author", "title", "content", "image","remark", "background","appreciation",
              "annotation","translation","click_num","fav_num",)
    list_display = ('title', 'author', "remark", 'fav_num', "click_num")
    raw_id_fields = ("author",)
    relfield_style = 'fk-ajax'
    list_select_related = ("author",)
    list_filter = ('author__dy',)
    search_fields = ('title', "author__name")
    ordering = ('fav_num', "click_num")
    readonly_fields = ("fav_num", "click_num")
    list_per_page = 50
    model_icon = "fa fa-book fa-fw"

    def get_form_layout(self):
        if self.org_obj:
            self.form_layout = (
                Main(
                    Fieldset('',
                             Row('title'),
                             Row('author'),
                             Row('remark'),
                             Row("fav_num", "click_num"),
                             Row('image'),
                             Row('content'),
                             ),
                    Fieldset('',
                             Row('background'),
                             Row('appreciation'),
                             Row('annotation'),
                             Row('translation')
                             ),
                ),
            )
        return super().get_form_layout()


class PoetAdmin:
    fields = ("name", "other_name", "dy", "born", "death", "fav_num", "click_num","work_num",
              "image","introduce","lifetime","achievement",)
    list_display = ('name', 'other_name', 'dy', 'born', 'death', 'fav_num', "click_num", "work_num")
    list_filter = ('dy',)
    search_fields = ('name',)
    ordering = ('fav_num', "click_num", "work_num")
    readonly_fields = ("click_num", "fav_num")
    relfield_style = 'fk-ajax'
    list_per_page = 50
    list_editable = ('dy', )
    model_icon = "fa fa-male"

    def get_form_layout(self):
        if self.org_obj:
            self.form_layout = (
                Main(
                    Fieldset('',
                             Row('name', 'dy'),
                             Row('other_name'),
                             Row('born', "death"),
                             Row("work_num","fav_num","click_num"),
                             Row('image'),
                             ),
                    Fieldset('',
                             Row('introduce'),
                             Row('lifetime'),
                             Row('achievement'),
                             ),
                )
            )
        return super().get_form_layout()


class PerfectPoemAdmin:
    list_display = ('poem', 'user', 'result', "add_time")
    raw_id_fields = ('poem', 'user')
    list_select_related = ("poem", "user")
    relfield_style = 'fk-ajax'
    show_detail_fields = ("poem", "user")
    readonly_fields = ("poem", "user", "add_time")
    list_filter = ('result',)
    list_editable = ('result', )
    ordering = ("-add_time",)
    list_per_page = 30

    def get_form_layout(self):
        if self.org_obj:
            self.form_layout = (
                Main(
                    Fieldset('',
                             Row('poem',"user"),
                             Row('tag'),
                             Row('image'),
                             Row('add_time'),
                             Row("result")
                             ),
                    Fieldset('',
                             Row('background'),
                             Row('appreciation'),
                             Row('annotation'),
                             Row('translation')
                             ),
                ),
            )
        return super().get_form_layout()


class PerfectPoetAdmin:
    list_display = ('poet', 'user', 'result', "add_time")
    raw_id_fields = ('poet', 'user')
    list_select_related = ("poet", "user")
    show_detail_fields = ("poet", "user")
    readonly_fields = ("poet", "user", "add_time")
    relfield_style = 'fk-ajax'
    list_filter = ('result',)
    list_editable = ('result',)
    ordering = ("-add_time",)
    list_per_page = 30

    def get_form_layout(self):
        if self.org_obj:
            self.form_layout = (
                Main(
                    Fieldset('',
                             Row('poet', 'user'),
                             Row('other_name'),
                             Row('born', "death"),
                             Row('image'),
                             Row("add_time"),
                             Row("result")
                             ),
                    Fieldset('',
                             Row('introduce'),
                             Row('lifetime'),
                             Row('achievement'),
                             ),
                )
            )
        return super().get_form_layout()


class AddPoemAdmin:
    list_display = ('title', 'author', "user", 'result', "add_time")
    raw_id_fields = ('user',)
    list_select_related = ("user",)
    show_detail_fields = ("user",)
    readonly_fields = ("user", "add_time")
    relfield_style = 'fk-ajax'
    list_filter = ('result',)
    list_editable = ('result',)
    ordering = ("-add_time",)
    list_per_page = 30

    def get_form_layout(self):
        if self.org_obj:
            self.form_layout = (
                Main(
                    Fieldset('',
                             Row('user'),
                             Row('title', 'author'),
                             Row('tag','image'),
                             Row('add_time'),
                             Row('result'),
                             ),
                    Fieldset('',
                             Row('content'),
                             Row('background'),
                             Row('appreciation'),
                             Row('annotation'),
                             Row('translation')
                             ),
                ),
            )
        return super().get_form_layout()


class AddPoetAdmin:
    list_display = ('name', 'dynasty', "user", 'result', "add_time")
    raw_id_fields = ('user',)
    list_select_related = ("user",)
    show_detail_fields = ("user",)
    readonly_fields = ("user", "add_time")
    relfield_style = 'fk-ajax'
    list_filter = ('result','dynasty')
    list_editable = ('result',)
    ordering = ("-add_time",)
    list_per_page = 30

    def get_form_layout(self):
        if self.org_obj:
            self.form_layout = (
                Main(
                    Fieldset('',
                             Row("user"),
                             Row('name', 'dynasty'),
                             Row('other_name'),
                             Row('born', "death"),
                             Row('image'),
                             Row("add_time"),
                             Row("result"),
                             ),
                    Fieldset('',
                             Row('introduce'),
                             Row('lifetime'),
                             Row('achievement'),
                             ),
                )
            )
        return super().get_form_layout()


xadmin.site.register(Poem, PoemAdmin)
xadmin.site.register(Poet, PoetAdmin)
xadmin.site.register(MingJu, MingJuAdmin)
xadmin.site.register(TaggedItem, TagAdmin)
xadmin.site.register(PerfectPoem, PerfectPoemAdmin)
xadmin.site.register(PerfectPoet, PerfectPoetAdmin)
xadmin.site.register(AddPoem, AddPoemAdmin)
xadmin.site.register(AddPoet, AddPoetAdmin)