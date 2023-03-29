from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated

from .permissions import IsOwner

from .models import (
    CollectPoem,
    CollectPoet,
    CollectDynamic,
    CollectArticle,
    FabulousDynamic,
    FabulousArticle,
    FollowTopic,
    FollowUser,

    LikeComment,
    DislikeComment
)
from .serializers import (
    CollectPoemSerializer,
    CollectPoetSerializer,
    CollectDynamicSerializer,
    CollectArticleSerializer,
    FabulousDynamicSerializer,
    FabulousArticleSerializer,
    FollowTopicSerializer,
    FollowUserSerializer,

    LikeCommentSerializer,
    DislikeCommentSerializer
)
User = get_user_model()
# Create your views here.


class CollectPoemViewSet(mixins.CreateModelMixin,
                         mixins.DestroyModelMixin,
                         viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = CollectPoemSerializer

    lookup_field = "poem_id" #根据该字段删除数据

    def get_queryset(self):
        return CollectPoem.objects.filter(user=self.request.user)


class CollectPoetViewSet(mixins.CreateModelMixin,
                         mixins.DestroyModelMixin,
                         viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = CollectPoetSerializer

    lookup_field = "poet_id"

    def get_queryset(self):
        return CollectPoet.objects.filter(user=self.request.user)


class CollectDynamicViewSet(mixins.CreateModelMixin,
                            mixins.DestroyModelMixin,
                            viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = CollectDynamicSerializer

    lookup_field = "dynamic_id"

    def get_queryset(self):
        return CollectDynamic.objects.filter(user=self.request.user)


class FabulousDynamicViewSet(mixins.CreateModelMixin,
                             mixins.DestroyModelMixin,
                             viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = FabulousDynamicSerializer

    lookup_field = "dynamic_id"

    def get_queryset(self):
        return FabulousDynamic.objects.filter(user=self.request.user)


class CollectArticleViewSet(mixins.CreateModelMixin,
                            mixins.DestroyModelMixin,
                            viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = CollectArticleSerializer

    lookup_field = 'article_id' # 根据article_id删除数据

    def get_queryset(self):
        return CollectArticle.objects.filter(user=self.request.user)


class FabulousArticleViewSet(mixins.CreateModelMixin,
                             mixins.DestroyModelMixin,
                             viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = FabulousArticleSerializer

    lookup_field = 'article_id'

    def get_queryset(self):
        return FabulousArticle.objects.filter(user=self.request.user)


class FollowTopicViewSet(mixins.CreateModelMixin,
                         mixins.DestroyModelMixin,
                         viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = FollowTopicSerializer

    lookup_field = 'topic_id'

    def get_queryset(self):
        return FollowTopic.objects.filter(user=self.request.user)


class FollowUserViewSet(mixins.CreateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = FollowUserSerializer

    lookup_field = 'followed_user_id'

    def get_queryset(self):
        return FollowUser.objects.filter(user=self.request.user)


class LikeCommentViewSet(mixins.CreateModelMixin,
                         mixins.DestroyModelMixin,
                         viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = LikeCommentSerializer

    lookup_field = 'comment_id'

    def get_queryset(self):
        return LikeComment.objects.filter(user=self.request.user)


class DislikeCommentViewSet(mixins.CreateModelMixin,
                         mixins.DestroyModelMixin,
                         viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = DislikeCommentSerializer

    lookup_field = 'comment_id'

    def get_queryset(self):
        return DislikeComment.objects.filter(user=self.request.user)

