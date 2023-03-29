from django.contrib.auth import get_user_model
from django.shortcuts import render_to_response, get_object_or_404
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status as http_status

from .serializers import (
    CardSerializer,
    RegisterSerializer,
    ForgetPasswordSerializer,
    UserInfomationSerializer,
    UserPersonalCenterSerializer,
    ChangePasswordSerializer,
    ChangeAvatarSerializer,
    IntegralSerializer,

    CollectPoemSerializer,
    CollectPoetSerializer,
    CollectDynamicSerializer,
    CollectArticleSerializer,
    FollowTopicSerializer,
    FanSerializer,
    FollowUserSerializer,
    TagSerializer,
    CommentSerializer
)
from community.serializers import DynamicListSerializer, ArticleSerializer

from operation.models import (
    CollectPoem,
    CollectPoet,
    CollectDynamic,
    CollectArticle,
    FollowTopic,
    FollowUser
)
from utils.mixins import IsOpRetrieveModelMixin

User = get_user_model()
# Create your views here.


class CardViewSet(mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = CardSerializer


class RegisterViewSet(mixins.CreateModelMixin,
                      viewsets.GenericViewSet):
    serializer_class = RegisterSerializer


class ForgetPasswordViewSet(mixins.UpdateModelMixin,
                            viewsets.GenericViewSet):
    serializer_class = ForgetPasswordSerializer
    queryset = User.objects.all()

    def update(self, request, *args, **kwargs):
        instance = get_object_or_404(User, email=request.data['email'])
        serializer = self.get_serializer(instance, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)

        password = serializer.validated_data["new_password"]
        instance.set_password(password)
        instance.save()
        return Response(status=http_status.HTTP_200_OK)


# 用户信息 无权限认证
class UserInformationViewSet(IsOpRetrieveModelMixin,
                             viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserInfomationSerializer

    foreign_model = "followed_user"
    OpModels = [FollowUser]
    op_fields = ["is_follow"]
    lookup_field = "uuid"

    @action(methods=['get'], detail=True, serializer_class=TagSerializer, url_path='tags',
            url_name='user-tags')
    def tags(self, request, uuid=None):
        user = get_object_or_404(User, uuid=uuid)
        queryset = user.tags.all()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=True, serializer_class=CommentSerializer, url_path='comments',
            url_name='user-comments')
    def comments(self, request, uuid=None):
        user = get_object_or_404(User, uuid=uuid)
        queryset = user.comment_set.filter(deleted=False).order_by("-add_time")
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=True, serializer_class=CollectPoemSerializer, url_path='collect-poems',
            url_name='user-collect-poems')
    def collect_poems(self, request, uuid=None):
        queryset = CollectPoem.objects.filter(user__uuid=uuid).order_by('-add_time')

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=True, serializer_class=CollectPoetSerializer, url_path='collect-poets',
            url_name='user-collect-poets')
    def collect_poets(self, request, uuid=None):
        queryset = CollectPoet.objects.filter(user__uuid=uuid).order_by('-add_time')

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=True, serializer_class=CollectDynamicSerializer, url_path='collect-dynamics',
            url_name='user-collect-dynamics')
    def collect_dynamics(self, request, uuid=None):
        queryset = CollectDynamic.objects.filter(user__uuid=uuid).order_by('-add_time')

        page = self.paginate_queryset(queryset)
        if page is not None:
            for instance in page:
                if instance.dynamic.deleted is True:
                    instance.dynamic.text = None
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        for instance in queryset:
            if instance.dynamic.deleted is True:
                instance.dynamic.text = None
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=True, serializer_class=CollectArticleSerializer, url_path='collect-articles',
            url_name='user-collect-articles')
    def collect_articles(self, request, uuid=None):
        queryset = CollectArticle.objects.filter(user__uuid=uuid).order_by('-add_time')

        page = self.paginate_queryset(queryset)
        if page is not None:
            for instance in page:
                if instance.article.deleted is True:
                    instance.article.title = None
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        for instance in queryset:
            if instance.article.deleted is True:
                instance.article.title = None
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=True, serializer_class=FollowTopicSerializer, url_path='follow-topics',
            url_name='user-follow-topics')
    def follow_topics(self, request, uuid=None):
        queryset = FollowTopic.objects.filter(user__uuid=uuid).order_by('-add_time')

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=True, serializer_class=FanSerializer, url_path='fans',
            url_name='user-fans')
    def fans(self, request, uuid=None):
        queryset = FollowUser.objects.filter(followed_user__uuid=uuid)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=True, serializer_class=FollowUserSerializer, url_path='followers',
            url_name='user-followers')
    def followers(self, request, uuid=None):
        queryset = FollowUser.objects.filter(user__uuid=uuid)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=True, serializer_class=DynamicListSerializer, url_path='dynamics',
            url_name='user-dynamics')
    def dynamics(self, request, uuid=None):
        user = get_object_or_404(User, uuid=uuid)
        queryset = user.dynamic_set.filter(deleted=False).order_by('-add_time')

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=True, serializer_class=ArticleSerializer, url_path='articles',
            url_name='user-articles')
    def articles(self, request, uuid=None):
        user = get_object_or_404(User, uuid=uuid)
        queryset = user.article_set.filter(deleted=False).order_by('-add_time')

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# 当前登录用户个人中心信息
class UserPersonalCenterViewSet(mixins.UpdateModelMixin,
                                viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserPersonalCenterSerializer

    def get_object(self):
        # get_object()：retrieve, update, destroy
        return self.request.user

    def get_queryset(self):
        # get_queryset()：list
        return [self.request.user]

    def list(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @action(methods=['post'], detail=False, serializer_class=ChangeAvatarSerializer, url_path='change-avatar',
            url_name='change-avatar')
    def change_avatar(self, request):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    @action(methods=['post'], detail=False, serializer_class=ChangePasswordSerializer, url_path='change-password', url_name='change-password')
    def set_password(self, request):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)

        old_password = serializer.validated_data["old_password"]
        new_password = serializer.validated_data["new_password"]
        if instance.check_password(old_password):
            if old_password == new_password:
                return Response({
                    "status_code":1,
                    "msg": "新密码不能与原密码相同"
                }, status=http_status.HTTP_400_BAD_REQUEST)
            instance.set_password(new_password)
            instance.save()
            return Response(status=http_status.HTTP_200_OK)
        return Response({
            "status_code": 2,
            "msg": "原密码不正确"
        }, status=http_status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, serializer_class=IntegralSerializer, url_path='integral',url_name='user-integral')
    def get_integral(self, request):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @action(methods=['get'], detail=False, serializer_class=TagSerializer, url_path='tags',
            url_name='user-tags')
    def tags(self, request):
        queryset = request.user.tags.all()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False, serializer_class=CommentSerializer, url_path='comments',
            url_name='user-comments')
    def comments(self, request):
        queryset = request.user.comment_set.filter(deleted=False).order_by("-add_time")
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False, serializer_class=CollectPoemSerializer, url_path='collect-poems',
            url_name='user-collect-poems')
    def collect_poems(self, request):
        queryset = CollectPoem.objects.filter(user=request.user).order_by('-add_time')

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False, serializer_class=CollectPoetSerializer, url_path='collect-poets',
            url_name='user-poets')
    def collect_poets(self, request):
        queryset = CollectPoet.objects.filter(user=request.user).order_by('-add_time')

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False, serializer_class=CollectDynamicSerializer, url_path='collect-dynamics',
            url_name='user-collect-dynamics')
    def collect_dynamics(self, request):
        queryset = CollectDynamic.objects.filter(user=request.user).order_by('-add_time')

        page = self.paginate_queryset(queryset)
        if page is not None:
            for instance in page:
                if instance.dynamic.deleted is True:
                    instance.dynamic.text = None
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        for instance in queryset:
            if instance.dynamic.deleted is True:
                instance.dynamic.text = None
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False, serializer_class=CollectArticleSerializer, url_path='collect-articles',
            url_name='user-collect-articles')
    def collect_articles(self, request):
        queryset = CollectArticle.objects.filter(user=request.user).order_by('-add_time')

        page = self.paginate_queryset(queryset)
        if page is not None:
            for instance in page:
                if instance.article.deleted is True:
                    instance.article.title = None
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        for instance in queryset:
            if instance.article.deleted is True:
                instance.article.title = None
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False, serializer_class=FollowTopicSerializer, url_path='follow-topics',
            url_name='user-follow-topics')
    def follow_topics(self, request):
        queryset = FollowTopic.objects.filter(user=request.user).order_by('-add_time')

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False, serializer_class=FanSerializer, url_path='fans',
            url_name='user-fans')
    def fans(self, request):
        queryset = FollowUser.objects.filter(followed_user=request.user)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False, serializer_class=FollowUserSerializer, url_path='followers',
            url_name='user-followers')
    def followers(self, request):
        queryset = FollowUser.objects.filter(user=request.user)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False, serializer_class=DynamicListSerializer, url_path='dynamics',
            url_name='user-dynamics')
    def dynamics(self, request):
        queryset = request.user.dynamic_set.filter(deleted=False).order_by('-add_time')

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False, serializer_class=ArticleSerializer, url_path='articles',
            url_name='user-articles')
    def articles(self, request):
        queryset = request.user.article_set.filter(deleted=False).order_by('-add_time')

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


def page_not_found(request, exception):
    #全局404处理函数
    response = render_to_response('404.html', {})
    response.status_code = 404
    return response

def page_error(request):
    #全局500处理函数
    response = render_to_response('500.html', {})
    response.status_code = 500
    return response