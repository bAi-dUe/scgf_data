from rest_framework import serializers

from .models import (
    Notification,
    Banner,
    Feedback
)


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ("id", "title", "content")


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ("title", "image", "url")


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        exclude = ("result", )