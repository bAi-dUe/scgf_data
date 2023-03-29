from datetime import date

from django.shortcuts import get_object_or_404
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from operation.permissions import IsOwner
from utils.mixins import (
    AddOneToClickNumAndIsOpRetrieveModelMixin,
    OpListModelMixin,
    LogicDestroyModelMixin
)
from .models import (
    Sign,
    Topic,
    Dynamic,
    Article,
    Comment
)
from .serializers import (
    SignSerializer,
    TopicSerializer,
    FilterTopicSerializer,

    DynamicListSerializer,
    DynamicRetrieveSerializer,
    DynamicCreateSerializer,
    DynamicDestroySerializer,

    UploadImageSerializer,

    ArticleSerializer,
    CommentListSerializer,
    ArticleCreateSerializer,
    ArticleDestroySerializer,

    CommentSerializer,
)
from utils.serializers import OnlyIdSerializer
from operation.models import (
    CollectDynamic,
    FabulousDynamic,
    CollectArticle,
    FabulousArticle,
    FollowTopic,
    LikeComment,
    DislikeComment
)


class SignViewSet(mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = SignSerializer

    @action(methods=['get'], detail=False, serializer_class=OnlyIdSerializer, url_path='is-sign',
            url_name='is-sign')
    def is_sign(self, request):
        today = date.today()
        instance = get_object_or_404(Sign, user=request.user, date=today)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class TopicViewSet(OpListModelMixin,
                   AddOneToClickNumAndIsOpRetrieveModelMixin,
                   viewsets.GenericViewSet):
    """
        `GET /topics/`: 话题列表 <br />
        `GET /topics/{pk}/`: 话题详情<br />
        `GET /topics/{pk}/dynamics/`: id为pk的话题下所有的动态<br />
    """
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    lookup_field = "uuid"

    foreign_model = "topic"
    OpModels = [FollowTopic]
    op_fields = ["is_follow"]
    filter_backends = [filters.SearchFilter]
    # filter_backends = (filters.OrderingFilter,)
    # ordering_fields = ('followed','nums')
    search_fields = ("topic",)

    @action(methods=['get'], detail=True, serializer_class=DynamicListSerializer, url_path='dynamics', url_name='dynamics-of-topic')
    def dynamics(self, request, uuid=None):
        queryset = Dynamic.objects.filter(topic__uuid=uuid, deleted=False)

        page = self.paginate_queryset(queryset)
        if page is not None:
            if request.user.is_authenticated:
                for dynamic in page:
                    if CollectDynamic.objects.filter(user=request.user,dynamic=dynamic).exists():
                        dynamic.is_collect = True
                    if FabulousDynamic.objects.filter(user=request.user, dynamic=dynamic).exists():
                        dynamic.is_fabulous = True
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        if request.user.is_authenticated:
            for dynamic in queryset:
                if CollectDynamic.objects.filter(user=request.user, dynamic=dynamic).exists():
                    dynamic.is_collect = True
                if FabulousDynamic.objects.filter(user=request.user, dynamic=dynamic).exists():
                    dynamic.is_fabulous = True
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class FilterTopicViewSet(mixins.ListModelMixin,
                         viewsets.GenericViewSet):
    queryset = Topic.objects.all()
    serializer_class = FilterTopicSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ("topic",)


class DynamicViewSet(OpListModelMixin,
                     AddOneToClickNumAndIsOpRetrieveModelMixin,
                     mixins.CreateModelMixin,
                     LogicDestroyModelMixin,
                     viewsets.GenericViewSet):
    queryset = Dynamic.objects.filter(deleted=False).order_by('-add_time')
    foreign_model = "dynamic"
    OpModels = [CollectDynamic, FabulousDynamic]
    op_fields = ["is_collect", "is_fabulous"]
    lookup_field = 'uuid'
    # filter_backends = (filters.OrderingFilter, )
    # ordering_fields = ("fabulous_num", "fav_num", "comment_num")

    @action(methods=['get'], detail=True, url_path='comments', url_name='article-comments')
    def comments(self, request, uuid=None):
        dynamic = get_object_or_404(Dynamic, uuid=uuid)
        queryset = dynamic.comments.filter(deleted=False).order_by("-add_time")
        page = self.paginate_queryset(queryset)
        if page is not None:
            if request.user.is_authenticated:
                for instance in page:
                    d = {
                        "user": request.user,
                        "comment": instance,
                    }
                    if LikeComment.objects.filter(**d).exists():
                        instance.is_like = True
                    if DislikeComment.objects.filter(**d).exists():
                        instance.is_dislike = True
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        if request.user.is_authenticated:
            for instance in queryset:
                d = {
                    "user": request.user,
                    "comment": instance,
                }
                if LikeComment.objects.filter(**d).exists():
                    instance.is_like = True
                if DislikeComment.objects.filter(**d).exists():
                    instance.is_dislike = True
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action == 'list':
            return DynamicListSerializer
        elif self.action == 'retrieve':
            return DynamicRetrieveSerializer
        elif self.action == 'create':
            return DynamicCreateSerializer
        elif self.action == "destroy":
            return DynamicDestroySerializer
        elif self.action == 'comments':
            return CommentListSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        elif self.action == "destroy":
            return [IsAuthenticated(), IsOwner()]
        else:
            return []


class ArticleViewSet(OpListModelMixin,
                     AddOneToClickNumAndIsOpRetrieveModelMixin,
                     mixins.CreateModelMixin,
                     LogicDestroyModelMixin,
                     viewsets.GenericViewSet):
    queryset = Article.objects.filter(deleted=False).order_by('-add_time')
    foreign_model = "article"
    OpModels = [CollectArticle, FabulousArticle]
    op_fields = ["is_collect", "is_fabulous"]
    lookup_field = "uuid"

    @action(methods=['get'], detail=True, url_path='comments', url_name='article-comments')
    def comments(self, request, uuid=None):
        article = get_object_or_404(Article, uuid=uuid)
        queryset = article.comments.filter(deleted=False).order_by("-add_time")
        page = self.paginate_queryset(queryset)
        if page is not None:
            if request.user.is_authenticated:
                for instance in page:
                    d = {
                        "user": request.user,
                        "comment": instance,
                    }
                    if LikeComment.objects.filter(**d).exists():
                        instance.is_like = True
                    if DislikeComment.objects.filter(**d).exists():
                        instance.is_dislike = True
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        if request.user.is_authenticated:
            for instance in queryset:
                d = {
                    "user": request.user,
                    "comment": instance,
                }
                if LikeComment.objects.filter(**d).exists():
                    instance.is_like = True
                if DislikeComment.objects.filter(**d).exists():
                    instance.is_dislike = True
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return ArticleSerializer
        elif self.action == 'create':
            return ArticleCreateSerializer
        elif self.action == "destroy":
            return ArticleDestroySerializer
        elif self.action == 'comments':
            return CommentListSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        elif self.action == "destroy":
            return [IsAuthenticated(), IsOwner()]
        else:
            return []


class UploadImageViewSet(mixins.CreateModelMixin,
                         viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UploadImageSerializer
    
    
class CommentViewSet(mixins.CreateModelMixin,
                     LogicDestroyModelMixin,
                     viewsets.GenericViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.filter(deleted=False)

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        elif self.action == "destroy":
            return [IsAuthenticated(), IsOwner()]
        else:
            return []

    @action(methods=['get'], detail=True, url_path='comments',serializer_class=CommentListSerializer, url_name='sub-comments')
    def comments(self, request, pk=None):
        comment = get_object_or_404(Comment, id=pk)
        queryset = comment.comments.filter(deleted=False).order_by("-add_time")
        page = self.paginate_queryset(queryset)
        if page is not None:
            if request.user.is_authenticated:
                for instance in page:
                    d = {
                        "user": request.user,
                        "comment": instance,
                    }
                    if LikeComment.objects.filter(**d).exists():
                        instance.is_like = True
                    if DislikeComment.objects.filter(**d).exists():
                        instance.is_dislike = True
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        if request.user.is_authenticated:
            for instance in queryset:
                d = {
                    "user": request.user,
                    "comment": instance,
                }
                if LikeComment.objects.filter(**d).exists():
                    instance.is_like = True
                if DislikeComment.objects.filter(**d).exists():
                    instance.is_dislike = True
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)