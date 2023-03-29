import xadmin

from .models import (
    MailVerifyCode,
    SMSVerifyCode
)


class MailVerifyCodeAdmin:
    list_display = ['code', 'email', 'code_type', 'send_time']
    list_per_page = 50
    search_fields = ('email',)
    ordering = ('-send_time',)
    model_icon = "fa fa-envelope"


class SMSVerifyCodeAdmin:
    list_display = ['code', 'phone', 'code_type', 'send_time']
    list_per_page = 50
    search_fields = ('phone',)
    ordering = ('-send_time',)
    model_icon = "fa fa-comment-o"


xadmin.site.register(MailVerifyCode, MailVerifyCodeAdmin)
xadmin.site.register(SMSVerifyCode, SMSVerifyCodeAdmin)