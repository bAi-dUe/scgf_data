from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.decorators import action

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


from .serializers import (
    PoetListSerializer,
    PoetRetrieveSerializer,
    PoemRetrieveSerializer,
    PoemListSerializer,
    ClassicPoemSerializer,
    MingJuSerializer,
    PoetAtlasSerializer,
    RecommandSerializer,
    TagSerializer,

    AddPoemSerializer,
    AddPoetSerializer,
    PerfectPoemSerializer,
    PerfectPoetSerializer
)
from .models import (
    Poet,
    Poem,
    MingJu,
    TaggedItem,
)

from operation.models import CollectPoem, CollectPoet

from utils.mixins import (
    AddOneToClickNumAndIsOpRetrieveModelMixin,
)
# Create your views here.


class PoetViewSet(mixins.ListModelMixin,
                  AddOneToClickNumAndIsOpRetrieveModelMixin,
                  viewsets.GenericViewSet):
    """
        `GET /poems/`: 诗人列表 <br />
        `GET /poems/{pk}/`: 诗人详情<br />
        `GET /poems/{pk}/poems`: id为pk的诗人的所有诗歌作品<br />
        `GET /poems/{pk}/atlas`: 获取id为pk的诗人的图谱信息<br />
    """
    queryset = Poet.objects.all().order_by('-click_num')
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filter_fields = ("dynasty",)
    search_fields = ("name",)
    ordering_fields = ('click_num', "fav_num", 'work_num', )

    foreign_model = "poet"
    OpModels = [CollectPoet]
    op_fields = ["is_collect"]

    lookup_field = "uuid"

    @method_decorator(cache_page(60 * 60 * 2))
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action == 'list':
            return PoetListSerializer
        elif self.action == 'retrieve':
            return PoetRetrieveSerializer
        elif self.action == 'poems':
            return PoemListSerializer
        elif self.action == 'classic':
            return ClassicPoemSerializer
        elif self.action == 'atlas':
            return PoetAtlasSerializer

    @action(methods=['get'], detail=True, url_path='poems', url_name='poet-works')
    def poems(self, request, uuid=None):
        queryset = Poem.objects.filter(author__uuid=uuid)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=True, url_path='classic', url_name='classic-works')
    def classic(self, request, uuid=None):
        queryset = Poem.objects.filter(author__uuid=uuid).order_by('-click_num')[:8]

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=True, url_path='atlas', url_name='poet-atlas')
    def atlas(self, request, uuid=None):
        instance = get_object_or_404(Poet, uuid=uuid)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class PoemViewSet(mixins.ListModelMixin,
                  AddOneToClickNumAndIsOpRetrieveModelMixin,
                  viewsets.GenericViewSet):
    """诗歌列表+搜索功能"""
    queryset = Poem.objects.all().order_by('-click_num')
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend)
    search_fields = ("title", "content")
    filter_fields = ("author__dynasty","author__name")
    ordering_fields = ("fav_num", "click_num")

    lookup_field = "uuid" # 根据uuid查找

    foreign_model = "poem"
    OpModels = [CollectPoem]
    op_fields = ["is_collect"]

    @method_decorator(cache_page(60 * 60 * 2))
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action == 'list':
            return PoemListSerializer
        elif self.action == 'retrieve':
            return PoemRetrieveSerializer


class MingJuViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """名句列表"""
    queryset = MingJu.objects.all()
    serializer_class = MingJuSerializer

    @method_decorator(cache_page(60 * 60 * 2))
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class PoemCategoryViewSet(mixins.ListModelMixin,
                          viewsets.GenericViewSet):
    serializer_class = PoemListSerializer

    def get_queryset(self):
        tag = self.request.GET.get('tag')
        if(tag):
            poem_type = ContentType.objects.get_for_model(Poem)
            poem_ids = TaggedItem.objects.filter(content_type=poem_type, tag__contains=tag).values_list("object_id")

            return Poem.objects.filter(id__in=poem_ids)

        return Poem.objects.all()

    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ("fav_num",)

    @method_decorator(cache_page(60 * 60 * 2))
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class RecommandViewSet(mixins.ListModelMixin,
                       viewsets.GenericViewSet):
    queryset = Poem.objects.filter(id__in=[29340, 48345, 48677])
    serializer_class = RecommandSerializer


class TagViewSet(mixins.CreateModelMixin,
                 mixins.DestroyModelMixin,
                 viewsets.GenericViewSet):
    serializer_class = TagSerializer
    queryset = TaggedItem.objects.all()


class AddPoemViewSet(mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    serializer_class = AddPoemSerializer


class AddPoetViewSet(mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    serializer_class = AddPoetSerializer


class PerfectPoemViewSet(mixins.CreateModelMixin,
                         viewsets.GenericViewSet):
    serializer_class = PerfectPoemSerializer


class PerfectPoetViewSet(mixins.CreateModelMixin,
                         viewsets.GenericViewSet):
    serializer_class = PerfectPoetSerializer
