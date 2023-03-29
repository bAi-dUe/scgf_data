from django.contrib import admin

from .models import (
    MailVerifyCode,
    SMSVerifyCode
)
# Register your models here.


@admin.register(MailVerifyCode)
class MailVerifyCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'email', 'code_type', 'send_time')
    search_fields = ('email', )
    list_per_page = 50
    ordering = ('-send_time',)


@admin.register(SMSVerifyCode)
class SMSVerifyCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'phone', 'code_type', 'send_time')
    search_fields = ('phone', )
    list_per_page = 50
    ordering = ('-send_time',)
