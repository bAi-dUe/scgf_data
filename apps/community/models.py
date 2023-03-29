import uuid as UUID

from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from poetry.models import TaggedItem

User = get_user_model()

# Create your models here.


class Sign(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    date = models.DateField(auto_now_add=True, verbose_name="签到日期")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="签到时间")

    class Meta:
        verbose_name = "每日签到"
        verbose_name_plural = verbose_name
        unique_together = ("user", "date")


class Topic(models.Model):
    uuid = models.UUIDField(unique=True, default=UUID.uuid4, editable=False)
    topic = models.CharField(max_length=20, unique=True, verbose_name="话题")
    image = models.ImageField(upload_to="Topic/%Y/%m/%d/", blank=True, verbose_name="图片", max_length=200)
    desc = RichTextField(verbose_name="描述")
    click_num = models.PositiveIntegerField(default=0, verbose_name="浏览量")
    followed = models.PositiveIntegerField(default=0, verbose_name="关注人数")
    nums = models.PositiveIntegerField(default=0, verbose_name="动态数")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    is_follow = models.BooleanField(default=False)

    tags = GenericRelation(TaggedItem)

    class Meta:
        verbose_name = "话题"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.topic


class Dynamic(models.Model):
    uuid = models.UUIDField(unique=True, default=UUID.uuid4, editable=False)
    topic = models.ForeignKey(Topic, blank=True, null=True, on_delete=models.CASCADE, verbose_name="话题")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    text = RichTextUploadingField(verbose_name="动态内容")
    click_num = models.PositiveIntegerField(default=0, verbose_name="浏览量")
    fabulous_num = models.PositiveIntegerField(default=0, verbose_name="赞")
    fav_num = models.PositiveIntegerField(default=0, verbose_name="收藏数")
    comment_num = models.PositiveIntegerField(default=0, verbose_name="评论数")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="发表时间")

    # deleted用于逻辑删除
    # deleting 判断是否正在执行删除操作
    deleted = models.BooleanField(default=False, verbose_name="已删除")
    deleting = models.BooleanField(default=False, verbose_name="正在删除")

    is_collect = models.BooleanField(default=False)
    is_fabulous = models.BooleanField(default=False)

    comments = GenericRelation('Comment')
    tags = GenericRelation(TaggedItem)

    class Meta:
        verbose_name = "动态"
        verbose_name_plural = verbose_name

    def __str__(self):
        if len(self.text)>20:
            return self.text[:20]+'...'
        return self.text[:20]


class Article(models.Model):
    uuid = models.UUIDField(unique=True, default=UUID.uuid4, editable=False)
    title = models.CharField(max_length=30, verbose_name="标题")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者")
    content = RichTextUploadingField(verbose_name="文章内容")
    click_num = models.PositiveIntegerField(default=0, verbose_name="浏览量")
    fabulous_num = models.PositiveIntegerField(default=0, verbose_name="赞")
    fav_num = models.PositiveIntegerField(default=0, verbose_name="收藏数")
    comment_num = models.PositiveIntegerField(default=0, verbose_name="评论数")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="发布时间")

    deleted = models.BooleanField(default=False, verbose_name="已删除")
    deleting = models.BooleanField(default=False, verbose_name="正在删除")

    is_collect = models.BooleanField(default=False)
    is_fabulous = models.BooleanField(default=False)

    comments = GenericRelation('Comment')
    tags = GenericRelation(TaggedItem)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name


class UploadImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="uploads/%Y/%m/%d", max_length=200)
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "上传图片"
        verbose_name_plural = verbose_name


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    like = models.PositiveIntegerField(default=0, verbose_name="顶")
    dislike = models.PositiveIntegerField(default=0, verbose_name="踩")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="时间")
    content = models.CharField(max_length=1000, verbose_name="评论内容")
    comment_num = models.PositiveIntegerField(default=0, verbose_name="评论数")

    deleted = models.BooleanField(default=False, verbose_name="已删除")
    deleting = models.BooleanField(default=False, verbose_name="正在删除")

    is_like = models.BooleanField(default=False)
    is_dislike= models.BooleanField(default=False)

    # 用于反向查询，不会生成表字段:评论的回复
    comments = GenericRelation('Comment')
    # 通用外键类型，什么类型外键都可以
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # 外键的id
    object_id = models.PositiveIntegerField()
    # 类型和id共同唯一确定一个对象
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self, ):
        return self.content

    def foreign_field(self):
        if isinstance(self.content_object, Article):
            if self.content_object.deleted is True:
                return None
            return self.content_object.title
        elif isinstance(self.content_object, Dynamic):
            if self.content_object.deleted is True:
                return None
            return self.content_object.text
        elif isinstance(self.content_object, Comment):
            return self.content_object.foreign_field()

    def foreign_type_string(self):
        if isinstance(self.content_object, Article):
            return 'article'
        elif isinstance(self.content_object, Dynamic):
            return 'dynamic'
        elif isinstance(self.content_object, Comment):
            return self.content_object.foreign_type_string()

    def object_uuid(self):
        if isinstance(self.content_object, (Article, Dynamic)):
            return self.content_object.uuid
        elif isinstance(self.content_object, Comment):
            return self.content_object.object_uuid()

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = verbose_name