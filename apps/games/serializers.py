from rest_framework import serializers

from .models import (
    PoemGenerate,
    PoemCompletion
)


class PoemCompletionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoemCompletion
        fields = "__all__"


class PoemGenerateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoemGenerate
        exclude = ("id", "create_time")