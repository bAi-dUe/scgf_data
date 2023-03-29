import uuid as UUID

from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser,BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MinLengthValidator
from django.contrib.contenttypes.fields import GenericRelation

from Shicigefu.settings import USERCARD_CONTENT_DEFAULT
from poetry.models import TaggedItem

# Create your models here.


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(unique=True, default=UUID.uuid4, editable=False)
    email = models.EmailField(unique=True, verbose_name="邮箱")
    is_staff = models.BooleanField(default=False, verbose_name="职工")
    is_active = models.BooleanField(default=True, verbose_name="账户状态")

    phone = models.CharField(max_length=11, blank=True, validators=[MinLengthValidator(11)], verbose_name="手机")
    nickname = models.CharField(max_length=20, verbose_name="昵称")
    designation = models.IntegerField(choices=(
                                          (1,"秀才"),
                                          (2, "举人"),
                                          (3, "进士"),
                                          (4, "探花"),
                                          (5, "榜眼"),
                                          (6, "状元"),
                                      ),
                                      default=1,
                                      verbose_name="称号")
    integral = models.PositiveIntegerField(default=0, verbose_name="积分")
    gender = models.SmallIntegerField(choices=((0,"男"), (1,"女")), default=0, verbose_name="性别")
    birthday = models.DateField(blank=True, null=True, verbose_name="生日")
    image = models.ImageField(upload_to="Avatar/%Y/%m/%d/", blank=True, max_length=200, default="Avatar/default.png", verbose_name="头像")
    signature = models.CharField(max_length=40, blank=True, verbose_name="个性签名")

    province = models.IntegerField(default=0, verbose_name="省份代码")
    city = models.IntegerField(default=0, verbose_name="城市代码")
    address = models.CharField(max_length=30, blank=True, verbose_name="地址")
    fans = models.PositiveIntegerField(default=0, verbose_name="粉丝数")
    follower = models.PositiveIntegerField(default=0, verbose_name="关注")
    fabulous_num = models.PositiveIntegerField(default=0, verbose_name="获赞")
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name="加入时间")

    is_follow = models.BooleanField(default=False)

    tags = GenericRelation(TaggedItem)

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["phone", "nickname"]

    objects = UserManager()

    def __str__(self):
        return self.email

    def follower_num(self):
        return self.user_fans.count()

    def fans_num(self):
        return self.user_follow.count()

    def get_full_name(self):
        return self.nickname

    def get_short_name(self):
        return self.nickname

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name


def _get_default_card_content():
    return USERCARD_CONTENT_DEFAULT


class Card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    bg_image = models.ImageField(max_length=200, blank=True, verbose_name="卡片背景图片")
    content = models.CharField(max_length=40, default=_get_default_card_content, verbose_name="内容")
    signature = models.CharField(max_length=10, default="诗词歌赋", verbose_name="落款")

    class Meta:
        verbose_name = "卡片"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.signature


