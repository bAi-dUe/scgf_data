from django.contrib import admin

from .models import User

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'nickname', 'phone', 'gender', 'is_active', 'is_staff',  'is_superuser', 'date_joined')
    list_filter = ('is_staff', 'is_superuser', 'is_active','gender', "designation")
    search_fields = ('email', 'nickname', 'phone')
    ordering = ('-date_joined',"integral")
    readonly_fields = ("fans", "follower", "fabulous_num","date_joined")
    filter_horizontal = ('groups', 'user_permissions',)
    exclude = ("is_follow",)
    list_per_page = 30

    fieldsets = (
        ("基本信息",{
                "fields":(
                    ("email","phone"),
                    ("nickname","image"),
                    ("gender","birthday"),
                    "signature",
                    ("date_joined", "last_login")
                )
        }),
        ("个人数据", {
            "fields": (
                ("integral", "designation"),
                ("fans", "follower", "fabulous_num"),
            )
        }),
        ("地址信息", {
            'fields': (
                ('province',"city"),
                'address'
            )
        }),
        ("权限和组", {
            'fields': (
                ('is_active', 'is_staff',  'is_superuser'),
                'groups',
                'user_permissions'
            )
        }),
    )


admin.site.site_header = '诗词歌赋系统后台'
admin.site.site_title = '诗词歌赋'
admin.site.site_url = "http://47.97.108.63:9090/"