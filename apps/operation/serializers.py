from rest_framework import serializers

from .models import (
    CollectPoem,
    CollectPoet,
    CollectDynamic,
    FabulousDynamic,
    CollectArticle,
    FabulousArticle,
    FollowTopic,
    FollowUser,

    LikeComment,
    DislikeComment
)


class CollectPoemSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = CollectPoem
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=CollectPoem.objects.all(),
                fields=("user", "poem"),
                message="已收藏"
            )
        ]
        fields = "__all__"


class CollectPoetSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = CollectPoet
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=CollectPoet.objects.all(),
                fields=("user", "poet"),
                message="已收藏"
            )
        ]
        fields = "__all__"


class CollectDynamicSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = CollectDynamic
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=CollectDynamic.objects.all(),
                fields=("user", "dynamic"),
                message="已关注"
            ),
        ]
        fields = "__all__"


class FabulousDynamicSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = FabulousDynamic
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=FabulousDynamic.objects.all(),
                fields=("user", "dynamic"),
                message="已关注"
            ),
        ]
        fields = "__all__"


class CollectArticleSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = CollectArticle
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=CollectArticle.objects.all(),
                fields=("user", "article"),
                message="已关注"
            ),
        ]
        fields = "__all__"


class FabulousArticleSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = FabulousArticle
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=FabulousArticle.objects.all(),
                fields=("user", "article"),
                message="已关注"
            ),
        ]
        fields = "__all__"


class FollowTopicSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = FollowTopic
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=FollowTopic.objects.all(),
                fields=("user", "topic"),
                message="已关注"
            ),
        ]
        fields = "__all__"


class FollowUserSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = FollowUser
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=FollowUser.objects.all(),
                fields=("user", "followed_user"),
                message="已关注"
            ),
        ]
        fields = "__all__"

    def validate(self, attrs):
        if attrs["user"] == attrs["followed_user"]:
            raise serializers.ValidationError("不能关注自己")
        return attrs


class LikeCommentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = LikeComment
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=LikeComment.objects.all(),
                fields=("user", "comment"),
                message="已点赞"
            ),
        ]
        fields = "__all__"


class DislikeCommentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = DislikeComment
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=DislikeComment.objects.all(),
                fields=("user", "comment"),
                message="已点赞"
            ),
        ]
        fields = "__all__"