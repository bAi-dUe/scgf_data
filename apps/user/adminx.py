from django.contrib.auth import get_user_model
from django.utils.translation import ugettext as _
import xadmin
from xadmin import views
from xadmin.layout import Fieldset, Main, Side, Row


User = get_user_model()

# Register your models here.
class BaseSetting:
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = '诗词歌赋'
    site_footer = '2020 诗词歌赋'
    site_url = '/'
    menu_style = 'accordion'


class UserAdmin:
    exclude = ("is_follow",)
    # fields = ("email", "nickname", "phone", "gender", "birthday","image", "signature",
    #           "date_joined","last_login", "integral","designation", "fans", "follower",
    #           "fabulous_num","province","city","address","is_active","is_staff","is_superuser",
    #           "groups","user_permissions")
    list_display = ('email', 'nickname', 'phone', 'gender', 'is_active', 'is_staff', 'is_superuser', 'date_joined')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'gender', "designation")
    search_fields = ('email', 'nickname', 'phone')
    ordering = ('-date_joined', "integral")
    readonly_fields = ("fans", "follower", "fabulous_num", "date_joined","last_login")
    filter_horizontal = ('groups', 'user_permissions',)
    list_per_page = 30
    relfield_style = 'fk-ajax'
    model_icon = 'fa fa-user'

    def get_form_layout(self):
        if self.org_obj:
            self.form_layout = (
                Main(
                    Fieldset('',
                             'email', 'password',
                             css_class='unsort no_title'
                             ),
                    Fieldset(_('Personal info'),
                             Row('email', 'phone'),
                             Row('nickname', 'image'),
                             Row('gender', 'birthday'),
                             "signature",
                             Row("date_joined", "last_login"),
                             ),
                    Fieldset(_('个人数据'),
                             Row('integral', 'designation'),
                             Row('fans', 'follower', "fabulous_num"),
                             ),
                    Fieldset(_('地址信息'),
                             Row('province', 'city'),
                             Row("address"),
                             ),
                    Fieldset(_('Permissions'),
                             'groups', 'user_permissions',
                             ),
                ),
                Side(
                    Fieldset(_('Status'),
                             'is_active', 'is_staff', 'is_superuser',
                             ),
                )
            )
        return super().get_form_layout()


xadmin.site.register(views.CommAdminView,GlobalSettings)
# xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.unregister(User)
xadmin.site.register(User, UserAdmin)