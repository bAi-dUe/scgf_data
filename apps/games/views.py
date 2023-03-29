import random

from rest_framework import viewsets
from rest_framework import mixins

from Shicigefu.settings import POEMCOMPLETION_MAX
from .models import (
    PoemCompletion,
    PoemGenerate
)
from .serializers import (
    PoemCompletionSerializer,
    PoemGenerateSerializer
)
# Create your views here.


class PoemCompletionViewSet(mixins.ListModelMixin,
                            viewsets.GenericViewSet):
    pcs = list(PoemCompletion.objects.all())
    serializer_class = PoemCompletionSerializer

    def get_queryset(self):
        queryset = random.sample(self.pcs, POEMCOMPLETION_MAX)
        return queryset


class PoemGenerateViewSet(mixins.ListModelMixin,
                          viewsets.GenericViewSet):
    """诗歌生成：
        `GET /poem-generate/?title={title}`
    """
    serializer_class = PoemGenerateSerializer

    def get_queryset(self):
        title = self.request.query_params.get('title')
        if title:
            return PoemGenerate.objects.all()[:1]
        return []