import xadmin

from .models import (
    PoemGenerate,
    PoemCompletion
)


class PoemGenerateAdmin:
    list_display = ['title', 'content', 'create_time']
    list_per_page = 50
    search_fields = ('title',)
    model_icon = 'fa fa-gamepad'


class PoemCompletionAdmin:
    list_display = ['question', 'answer', 'other1', 'other2', 'other3']
    list_per_page = 50
    search_fields = ('question',)
    list_editable = ['question', 'answer', 'other1', 'other2', 'other3']
    model_icon = "fa fa-puzzle-piece"


xadmin.site.register(PoemGenerate, PoemGenerateAdmin)
xadmin.site.register(PoemCompletion, PoemCompletionAdmin)
