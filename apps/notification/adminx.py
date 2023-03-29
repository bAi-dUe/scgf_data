import xadmin

from .models import Notification, Banner, Feedback


class NotificationAdmin:
    list_display = ('title', 'content', 'push', 'add_time',)
    list_editable = ("push", )
    ordering = ("-add_time",)
    list_per_page = 30


class BannerAdmin:
    list_display = ('title', 'url', 'index', "show", "add_time")
    list_per_page = 30
    list_editable = ("index", "url", "show")


class FeedbackAdmin:
    list_display = ('subject', 'user', 'contact', "result", "add_time")
    list_per_page = 30
    list_editable = ("result",)


xadmin.site.register(Notification, NotificationAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(Feedback, FeedbackAdmin)