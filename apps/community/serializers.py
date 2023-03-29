from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import (
    Sign,
    Topic,
    Dynamic,
    Article,
    UploadImage,
    Comment,
)

User = get_user_model()


class SignSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Sign
        fields = "__all__"


class TopicSerializer(serializers.ModelSerializer):
    is_follow = serializers.BooleanField(default=False)

    class Meta:
        model = Topic
        fields = "__all__"


class FilterTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ("id", "topic")


class _UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "uuid", 'nickname', 'image', "designation")


class _TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ("uuid", "topic")


class DynamicListSerializer(serializers.ModelSerializer):
    user = _UserSerializer()
    is_collect = serializers.BooleanField(default=False, read_only=True)
    is_fabulous = serializers.BooleanField(default=False, read_only=True)

    class Meta:
        model = Dynamic
        fields = ("id", "uuid", "user", "text", "click_num", "fabulous_num", "fav_num", "comment_num",
                  "add_time", "is_collect", "is_fabulous")


class DynamicRetrieveSerializer(serializers.ModelSerializer):
    topic = _TopicSerializer()
    user = _UserSerializer()

    class Meta:
        model = Dynamic
        # fields = "__all__"
        exclude = ("deleted","deleting")


class DynamicCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Dynamic
        fields = ("id", "uuid", 'user', 'topic', 'text', "add_time")


class DynamicDestroySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Dynamic
        fields = ("user", "id")


TopicAllDynamicsSerializer = DynamicListSerializer


class ArticleSerializer(serializers.ModelSerializer):
    user = _UserSerializer()
    is_collect = serializers.BooleanField(default=False, read_only=True)
    is_fabulous = serializers.BooleanField(default=False, read_only=True)

    class Meta:
        model = Article
        # fields = "__all__"
        exclude = ("deleted", 'deleting')


class ArticleCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Article
        fields = ("user", "title", "content")


class ArticleDestroySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Article
        fields = ("user", "id")


class CommentListSerializer(serializers.ModelSerializer):
    user = _UserSerializer()

    class Meta:
        model = Comment
        # fields = ("id", "user", "like", "dislike", "content", "foreign_field", "comment_num",
        #           "add_time","is_like","is_dislike")
        # fields = "__all__"
        exclude = ("deleted", 'deleting')


class UploadImageSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = UploadImage
        fields = ("user", "image")


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    content = serializers.CharField(max_length=1000)
    like = serializers.IntegerField(read_only=True)
    dislike = serializers.IntegerField(read_only=True)
    is_like = serializers.BooleanField(read_only=True)
    is_dislike = serializers.BooleanField(read_only=True)
    comment_num = serializers.IntegerField(read_only=True)
    # foreign_field = serializers.CharField(read_only=True)
    # object_uuid = serializers.UUIDField(read_only=True)
    # foreign_type_string = serializers.CharField(default='',read_only=True)

    class Meta:
        model = Comment
        # fields = "__all__"
        exclude = ("deleted", "deleting")

    def validate(self, attrs):
        content_type = attrs["content_type"]
        # 34 comment
        # 29 article
        # 16 dynamic
        # 15 topic
        # 8 poem
        # 7 poet
        # 6 user
        if content_type.id not in [16, 29, 34]:
            raise serializers.ValidationError({
                "status_code": 22,
                "msg": "错误的操作"
            })
        return attrs