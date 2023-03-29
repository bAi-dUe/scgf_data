from datetime import timedelta, datetime

from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from verifycode.models import MailVerifyCode
from operation.models import (
    CollectPoem,
    CollectPoet,
    CollectDynamic,
    CollectArticle,
    FollowTopic,
    FollowUser
)
from poetry.models import (
    Poem,
    Poet,
    TaggedItem
)
from community.models import (
    Dynamic,
    Article,
    Topic,
    Comment
)

from .models import Card
User = get_user_model()


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = "__all__"


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True,
                                   label="邮箱",
                                   validators=[UniqueValidator(User.objects.all(), message="该邮箱已注册")])
    nickname = serializers.CharField(required=True, max_length=20, label="昵称")
    gender = serializers.IntegerField(required=True,
                                     label="性别",
                                     help_text='(0,"男"), (1,"女")')
    code = serializers.CharField(required=True, write_only=True, max_length=6, min_length=6,
                                 error_messages={
                                     "blank": "请输入验证码",
                                     "required": "请输入验证码",
                                     "max_length": "验证码格式错误",
                                     "min_length": "验证码格式错误"
                                 },
                                 label="邮箱验证码",
                                 help_text="发送验证码接口为/verify/")
    password = serializers.CharField(max_length=16, min_length=8,
                                     label="密码",
                                     style={'input_type': "password"},
                                     write_only=True)

    def validate(self, attrs):
        """1：验证邮箱验证码是否正确
           2：将验证码字段从注册信息中删除——因为User中无code字段
        """
        code = attrs["code"]
        email = attrs["email"]
        verify_codes = MailVerifyCode.objects.filter(email=email,code=code,code_type=0).order_by('-send_time')[:1]
        if verify_codes.exists():
            verify_code = verify_codes[0]
            delta = timedelta(minutes=5)
            if verify_code.send_time+delta < datetime.now():
                raise serializers.ValidationError({
                    "status_code": 2,
                    "msg": "验证码已失效",
                })
        else:
            raise serializers.ValidationError({
                "status_code": 1,
                "msg": "验证码错误"
            })

        del attrs["code"]
        return attrs

    class Meta:
        model = User
        fields = ("email","nickname","password","gender","code")


class ForgetPasswordSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, write_only=True, label="邮箱")
    code = serializers.CharField(required=True, write_only=True, max_length=6, min_length=6,
                                 error_messages={
                                     "blank": "请输入验证码",
                                     "required": "请输入验证码",
                                     "max_length": "验证码格式错误",
                                     "min_length": "验证码格式错误"
                                 },
                                 label="邮箱验证码",
                                 help_text="发送验证码接口为/verify/")
    new_password = serializers.CharField(max_length=16, min_length=8,
                                         label="新密码",
                                         style={"input_type": "password"},
                                         write_only=True)

    class Meta:
        model = User
        fields = ("email", "code", "new_password")

    def validate(self, attrs):
        """1：验证邮箱验证码是否正确
           2：将验证码字段从注册信息中删除——因为User中无code字段
        """
        code = attrs["code"]
        email = attrs["email"]
        new_password = attrs['new_password']
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError({
                "status_code": 4,
                "msg": "此邮箱未注册"
            })
        verify_codes = MailVerifyCode.objects.filter(email=email, code=code, code_type=1).order_by('-send_time')[:1]
        if verify_codes.exists():
            verify_code = verify_codes[0]
            delta = timedelta(minutes=5)
            if verify_code.send_time + delta < datetime.now():
                raise serializers.ValidationError({
                    "status_code": 5,
                    "msg": "验证码已失效",
                })
            # else:
            #     user = User.objects.get(email=email)
            #     user.set_password(new_password)
            #     user.save()
        else:
            raise serializers.ValidationError({
                "status_code": 1,
                "msg": "验证码错误"
            })
        return attrs


class UserInfomationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "nickname", "gender", "image", "signature", "designation", "integral","is_follow",
                  "address", "fans", "follower", "fabulous_num", "date_joined", "is_active")


class UserPersonalCenterSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(read_only=True)
    image = serializers.ImageField(read_only=True)
    fans = serializers.IntegerField(read_only=True)
    follower = serializers.IntegerField(read_only=True)
    fabulous_num = serializers.IntegerField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)
    last_login = serializers.DateTimeField(read_only=True)
    date_joined = serializers.DateTimeField(read_only=True)
    designation = serializers.IntegerField(read_only=True)
    integral = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = ("id", "uuid", "email", "nickname", "gender", "designation", "integral", "birthday", "image",
                  "signature", "address", "fans", "follower", "fabulous_num", "is_active", "last_login", "date_joined")


class IntegralSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("integral", "designation")


class ChangeAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("image",)


class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(max_length=16, min_length=8,
                                         label="旧密码",
                                         style={"input_type": "password"},
                                         write_only=True)
    new_password = serializers.CharField(max_length=16, min_length=8,
                                         label="新密码",
                                         style={"input_type": "password"},
                                         write_only=True)

    class Meta:
        model = User
        fields = ("old_password","new_password")


class _PoemAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poet
        fields = ("id", "uuid", "name", "dynasty", "image")


class _PoemSerializer(serializers.ModelSerializer):
    author = _PoemAuthorSerializer()

    class Meta:
        model = Poem
        fields = ("id", "uuid", "author", "title")


class CollectPoemSerializer(serializers.ModelSerializer):
    poem = _PoemSerializer()

    class Meta:
        model = CollectPoem
        fields = ("id", "poem")


class _PoetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poet
        fields = ("id", "uuid", "name", "dynasty", "image", "other_name")


class CollectPoetSerializer(serializers.ModelSerializer):
    poet = _PoetSerializer()

    class Meta:
        model = CollectPoet
        fields = ("id", "poet")


class _UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "uuid", "nickname", "image", "designation")


class _DynamicSerializer(serializers.ModelSerializer):
    user = _UserSerializer()

    class Meta:
        model = Dynamic
        fields = ("id", "uuid", "user", "text", "add_time")


class CollectDynamicSerializer(serializers.ModelSerializer):
    dynamic = _DynamicSerializer()

    class Meta:
        model = CollectDynamic
        fields = ("id", "dynamic")


class _ArticleSerializer(serializers.ModelSerializer):
    user = _UserSerializer()

    class Meta:
        model = Article
        fields = ("id", "uuid", "title", "user", "add_time")


class CollectArticleSerializer(serializers.ModelSerializer):
    article = _ArticleSerializer()

    class Meta:
        model = CollectArticle
        fields = ("id", "article")


class _TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ("id", "uuid", "topic", "image", "desc")


class FollowTopicSerializer(serializers.ModelSerializer):
    topic = _TopicSerializer()

    class Meta:
        model = FollowTopic
        fields = ("id", "topic")


class FanSerializer(serializers.ModelSerializer):
    user = _UserSerializer()

    class Meta:
        model = FollowUser
        fields = ("id", "user")


class FollowUserSerializer(serializers.ModelSerializer):
    followed_user = _UserSerializer()

    class Meta:
        model = FollowUser
        fields = ("id", "followed_user")


class DynamicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dynamic
        fields = ("id", "text", "click_num", "fabulous_num", "fav_num", "comment_num", "add_time")


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("id", "title", "content", "click_num", "fabulous_num", "fav_num", "comment_num", "add_time")


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaggedItem
        fields = ("id", "tag")


class CommentSerializer(serializers.ModelSerializer):
    user = _UserSerializer()
    foreign_field = serializers.CharField(read_only=True)
    object_uuid = serializers.UUIDField(read_only=True)
    foreign_type_string = serializers.CharField(default='', read_only=True)

    class Meta:
        model = Comment
        # fields = ("id", "user", "like", "dislike", "content", "foreign_field", "comment_num",
        #           "add_time","is_like","is_dislike")
        # fields = "__all__"
        exclude = ("deleted","deleting")