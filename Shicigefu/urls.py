"""Shicigefu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
# serve代理MEDIA_ROOT
from django.views.static import serve
from django.conf import settings

from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
import xadmin

from Shicigefu.settings import MEDIA_ROOT
from poetry.views import (
    PoetViewSet,
    PoemViewSet,
    MingJuViewSet,
    PoemCategoryViewSet,
    RecommandViewSet,
    TagViewSet,
    AddPoemViewSet,
    AddPoetViewSet,
    PerfectPoemViewSet,
    PerfectPoetViewSet
)
from games.views import (
    PoemCompletionViewSet,
    PoemGenerateViewSet
)
from verifycode.views import (
    MailVerifyCodeViewSet
)
from user.views import (
    RegisterViewSet,
    ForgetPasswordViewSet,
    UserInformationViewSet,
    UserPersonalCenterViewSet,
    CardViewSet
)
from community.views import (
    SignViewSet,
    TopicViewSet,
    FilterTopicViewSet,
    DynamicViewSet,
    ArticleViewSet,
    UploadImageViewSet,
    CommentViewSet
)
from operation.views import (
    CollectPoemViewSet,
    CollectPoetViewSet,
    CollectDynamicViewSet,
    CollectArticleViewSet,
    FabulousDynamicViewSet,
    FabulousArticleViewSet,
    FollowTopicViewSet,
    FollowUserViewSet,
    LikeCommentViewSet,
    DislikeCommentViewSet
)

from notification.views import (
    NotificationViewSet,
    BannerViewSet,
    FeedbackViewSet
)

router_v1 = DefaultRouter()

#poetry
router_v1.register(r'poets', PoetViewSet, base_name="poet")
router_v1.register(r'poems', PoemViewSet, base_name="poem")
router_v1.register(r'mingju', MingJuViewSet, base_name="mingju")
router_v1.register(r'recommand', RecommandViewSet, base_name="recommand")
router_v1.register(r'tag', TagViewSet, base_name="tag")
router_v1.register(r'add-poem', AddPoemViewSet, base_name="add-poem")
router_v1.register(r'add-poet', AddPoetViewSet, base_name="add-poet")
router_v1.register(r'perfect-poem', PerfectPoemViewSet, base_name="perfect-poem")
router_v1.register(r'perfect-poet', PerfectPoetViewSet, base_name="perfect-poet")

#games
router_v1.register(r'game-completion', PoemCompletionViewSet, base_name="game-completion")
router_v1.register(r'game-generate', PoemGenerateViewSet, base_name="game-generate")

#user
router_v1.register(r'register', RegisterViewSet, base_name="register")
router_v1.register(r'forget-password', ForgetPasswordViewSet, base_name="forget-password")
router_v1.register(r'users', UserInformationViewSet, base_name="user-infomation")
router_v1.register(r'personal', UserPersonalCenterViewSet, base_name="personal-center")
router_v1.register(r'card', CardViewSet, base_name="user-card")

#verifycode
router_v1.register(r'verifycode-email', MailVerifyCodeViewSet, base_name="verifycode-email")

#community
router_v1.register(r'topics', TopicViewSet, base_name="topic")
router_v1.register(r'articles', ArticleViewSet, base_name="article")
router_v1.register(r'dynamics', DynamicViewSet, base_name="dynamic")
router_v1.register(r'comment', CommentViewSet, base_name="comment")
router_v1.register(r'upload-img', UploadImageViewSet, base_name="upload-img")
router_v1.register(r'sign', SignViewSet, base_name="sign")

# operation
router_v1.register(r'collect-poem', CollectPoemViewSet, base_name="collect-poem")
router_v1.register(r'collect-poet', CollectPoetViewSet, base_name="collect-poet")
router_v1.register(r'collect-dynamic', CollectDynamicViewSet, base_name="collect-dynamic")
router_v1.register(r'fabulous-dynamic', FabulousDynamicViewSet, base_name="fabulous-dynamic")
router_v1.register(r'collect-article', CollectArticleViewSet, base_name="collect-article")
router_v1.register(r'fabulous-article', FabulousArticleViewSet, base_name="fabulous-article")
router_v1.register(r'follow-topic', FollowTopicViewSet, base_name="follow-topic")
router_v1.register(r'follow-user', FollowUserViewSet, base_name="follow-user")
router_v1.register(r'like-comment', LikeCommentViewSet, base_name="like-comment")
router_v1.register(r'dislike-comment', DislikeCommentViewSet, base_name="dislike-comment")


router_v1.register(r'notification', NotificationViewSet, base_name="notification")
router_v1.register(r'banner', BannerViewSet, base_name="banner")
router_v1.register(r'feedback', FeedbackViewSet, base_name="feedback")

router_v1.register(r's/topics', FilterTopicViewSet, base_name="search-topic")
router_v1.register(r's/poems', PoemCategoryViewSet, base_name="poet-category")

# xadmin.autodiscover()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),

    # path('docs/', include_docs_urls(title="诗词歌赋")),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/v1/', include(router_v1.urls), name="api-v1"),

    # 第三方登录url
    # 访问 /login/{社交软件名}/ 即可跳转到第三方登录。
    url('', include('social_django.urls', namespace='social')),

    url(r'^media/(?P<path>.*)$', serve, {'document_root':MEDIA_ROOT}, name="media"),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}, name='static'),

    url(r'^api/token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^api/token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),

    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]



handler404 = 'user.views.page_not_found'
handler500 = 'user.views.page_error'