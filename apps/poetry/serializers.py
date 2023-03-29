from rest_framework import serializers

from .models import (
    Poem,
    Poet,
    MingJu,
    TaggedItem,
    AddPoet,
    AddPoem,
    PerfectPoet,
    PerfectPoem
)


class PoetListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poet
        fields = ("uuid", "name","image", "dynasty", "other_name", "introduce")


class PoetRetrieveSerializer(serializers.ModelSerializer):
    is_collect = serializers.BooleanField(default=False)

    class Meta:
        model = Poet
        exclude = ("remark", "dy", "born", "death")


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poet
        fields = ("uuid", "name", "dynasty", "image")


class PoemListSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Poem
        fields = ("uuid", "author", "title", "content", "remark")


class PoemRetrieveSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Poem
        fields = "__all__"


class ClassicPoemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poem
        fields = ("uuid", "title",)


class PoetAtlasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poet
        fields = ("name", "dynasty", "other_name", "born", "death", "fav_num", "work_num")


class MingJuSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = MingJu
        fields = ("title", "poem_uuid", "content", "author")


class RecommandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poem
        fields = ("uuid", "image")


class TagSerializer(serializers.ModelSerializer):
    tag = serializers.CharField(max_length=12, min_length=1)

    class Meta:
        model = TaggedItem
        fields = ("tag", "content_type", "object_id")

    def validate(self, attrs):
        content_type = attrs["content_type"]
        # 29 article
        # 16 dynamic
        # 15 topic
        # 8 poem
        # 7 poet
        # 6 user
        if content_type.id not in [6,7,8,15,16,29]:
            raise serializers.ValidationError({
                    "status_code": 22,
                    "msg": "错误的操作"
                })

        return attrs


class AddPoemSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddPoem
        exclude = ("result",)


class AddPoetSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddPoet
        exclude = ("result",)


class PerfectPoemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfectPoem
        exclude = ("result",)


class PerfectPoetSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfectPoet
        exclude = ("result",)
