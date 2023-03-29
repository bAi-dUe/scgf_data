from django.contrib import admin

from .models import (
    Notification,
    Banner,
    Feedback
)
# Register your models here.


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'push', 'add_time',)
    ordering = ("-add_time",)
    list_editable = ("push",)
    list_per_page = 30


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'index', "show", "add_time")
    list_per_page = 30
    list_editable = ("index", "show")
    fieldsets = (
        (None, {
            "fields": (
                "title",
                "url",
                "image",
                ("index","show"),
            )
        }),
    )


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('subject', 'user', 'desc','contact','result', 'add_time',)
    ordering = ("-add_time",)
    raw_id_fields = ('user', )
    list_editable = ("result",)
    list_per_page = 30
    list_filter = ("result",)