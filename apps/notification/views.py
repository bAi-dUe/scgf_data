from rest_framework import mixins
from rest_framework import viewsets

from .serializers import (
    NotificationSerializer,
    BannerSerializer,
    FeedbackSerializer
)
from .models import (
    Notification,
    Banner,
)


class NotificationViewSet(mixins.ListModelMixin,
                          viewsets.GenericViewSet):
    serializer_class = NotificationSerializer
    queryset = Notification.objects.filter(push=True)


class BannerViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = BannerSerializer
    queryset = Banner.objects.filter(show=True).order_by("index")


class FeedbackViewSet(mixins.CreateModelMixin,
                      viewsets.GenericViewSet):
    serializer_class = FeedbackSerializer
