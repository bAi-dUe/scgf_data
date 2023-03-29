import uuid as UUID

from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from ckeditor.fields import RichTextField

# Create your models here.


class TaggedItem(models.Model):
    tag = models.CharField(max_length=12, validators=[MinLengthValidator(1)], verbose_name="标签")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.tag

    def obj(self):
        return self.content_object

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name
        unique_together = ("tag", "content_type", "object_id")


class Poet(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(unique=True, default=UUID.uuid4, editable=False)
    name = models.CharField(max_length=20, verbose_name="姓名", db_index=True)
    dynasty = models.CharField(max_length=10,
                               choices=(
                                   ("未知", "未知"),
                                   ("唐代", "唐代"),
                                   ("宋代", "宋代"),
                                   ("元代", "元代"),
                                   ("明代", "明代"),
                                   ("清代", "清代"),
                                   ("先秦", "先秦"),
                                   ("两汉", "两汉"),
                                   ("魏晋", "魏晋"),
                                   ("南北朝", "南北朝"),
                                   ("隋代", "隋代"),
                                   ("五代", "五代"),
                                   ("辽朝", "辽朝"),
                                   ("金朝", "金朝"),
                                   ("近代", "近代"),
                                   ("现当代", "现当代")
                               ),
                               default="未知",
                               verbose_name="朝代")
    dy = models.IntegerField(default=0,
                             choices=(
                                 (0, "未知"),
                                 (1, "唐代"),
                                 (2, "宋代"),
                                 (3, "元代"),
                                 (4, "明代"),
                                 (5, "清代"),
                                 (6, "先秦"),
                                 (7, "两汉"),
                                 (8, "魏晋"),
                                 (9, "南北朝"),
                                 (10, "隋代"),
                                 (11, "五代"),
                                 (12, "辽朝"),
                                 (13, "金朝"),
                                 (14, "近代"),
                                 (15, "现当代")
                             ),verbose_name="朝代")
    other_name = models.CharField(max_length=50, blank=True, null=True, verbose_name="别称")
    image = models.ImageField(upload_to="Poet/%Y/%m/%d/", blank=True, default="Poet/default.png",max_length=200, verbose_name="肖像")
    born = models.IntegerField(blank=True, null=True, verbose_name="生于")
    death = models.IntegerField(blank=True, null=True, verbose_name="卒于")
    introduce = RichTextField(blank=True, verbose_name="简介")
    lifetime = RichTextField(blank=True, verbose_name="生平")
    achievement = RichTextField(blank=True, verbose_name="成就")
    remark = models.IntegerField(unique=True, null=True, default=-1)
    click_num = models.PositiveIntegerField(default=0, verbose_name="浏览量")
    fav_num = models.PositiveIntegerField(default=0, verbose_name="收藏数")
    work_num = models.PositiveIntegerField(default=0, verbose_name="收录作品数")

    is_collect = models.BooleanField(default=False)

    tags = GenericRelation(TaggedItem)

    class Meta:
        verbose_name = "诗人"
        verbose_name_plural = verbose_name

    def get_works_count(self):
        return self.poem_set.all().count()

    def __str__(self):
        return "{}[{}]".format(self.name, self.dynasty)


class Poem(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(unique=True, default=UUID.uuid4, editable=False)
    author = models.ForeignKey('Poet', on_delete=models.CASCADE, verbose_name="作者")
    title = models.CharField(max_length=50, verbose_name="标题", db_index=True)
    content = RichTextField(verbose_name="内容")
    image = models.ImageField(upload_to="Poem/%Y/%m/%d/", blank=True, default="Poem/default.png",max_length=200, verbose_name="情景图片")
    remark = models.CharField(max_length=300, blank=True, verbose_name="标签")
    background = RichTextField(blank=True, verbose_name="背景")
    appreciation = RichTextField(blank=True, verbose_name="鉴赏")
    annotation = RichTextField(blank=True, verbose_name="注解")
    translation = RichTextField(blank=True, verbose_name="译文")
    click_num = models.PositiveIntegerField(default=0, verbose_name="浏览量")
    fav_num = models.PositiveIntegerField(default=0, verbose_name="收藏数")

    is_collect = models.BooleanField(default=False)

    tags = GenericRelation(TaggedItem)

    class Meta:
        verbose_name = "诗歌"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def author_name(self):
        return self.author.name

    def author_dynasty(self):
        return self.author.dynasty


class MingJu(models.Model):
    poem = models.ForeignKey('Poem', on_delete=models.CASCADE, verbose_name="诗歌")
    title = models.CharField(max_length=50, verbose_name="标题")
    content = models.CharField(max_length=50, verbose_name="名句")

    tags = GenericRelation(TaggedItem)

    class Meta:
        verbose_name = "名句"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content

    def poem_uuid(self):
        return self.poem.uuid

    def author(self):
        return self.poem.author


class AddPoem(models.Model):
    user = models.ForeignKey('user.User', blank=True, null=True, on_delete=models.CASCADE, verbose_name="用户")
    title = models.CharField(max_length=50, verbose_name="标题")
    author = models.CharField(max_length=20, verbose_name="作者")
    content = RichTextField(verbose_name="内容")
    image = models.ImageField(upload_to="Poem/add/%Y/%m/%d/", blank=True, default="Poem/default.png", max_length=200, verbose_name="情景图片")
    tag = models.CharField(max_length=300, blank=True, verbose_name="标签")
    background = RichTextField(blank=True, verbose_name="背景")
    appreciation = RichTextField(blank=True, verbose_name="鉴赏")
    annotation = RichTextField(blank=True, verbose_name="注解")
    translation = RichTextField(blank=True, verbose_name="译文")
    result = models.SmallIntegerField(default=0,
                                      choices=(
                                          (0,"待处理"),
                                          (1,"已收录"),
                                          (2,"暂不收录")
                                      ),verbose_name="处理结果")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        verbose_name = "诗歌推荐收录"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s-%s"%(self.author,self.title)


class AddPoet(models.Model):
    user = models.ForeignKey('user.User', blank=True, null=True, on_delete=models.CASCADE, verbose_name="用户")
    name = models.CharField(max_length=20, verbose_name="姓名")
    dynasty = models.IntegerField(choices=(
                                 (0, "未知"),
                                 (1, "唐代"),
                                 (2, "宋代"),
                                 (3, "元代"),
                                 (4, "明代"),
                                 (5, "清代"),
                                 (6, "先秦"),
                                 (7, "两汉"),
                                 (8, "魏晋"),
                                 (9, "南北朝"),
                                 (10, "隋代"),
                                 (11, "五代"),
                                 (12, "辽朝"),
                                 (13, "金朝"),
                                 (14, "近代"),
                                 (15, "现当代")
                             ), verbose_name="朝代")
    other_name = models.CharField(max_length=50, blank=True, null=True, verbose_name="别称")
    image = models.ImageField(upload_to="Poet/add/%Y/%m/%d/", blank=True, default="Poet/default.png", max_length=200, verbose_name="肖像")
    born = models.IntegerField(blank=True, null=True, verbose_name="生于")
    death = models.IntegerField(blank=True, null=True, verbose_name="卒于")
    introduce = RichTextField(blank=True, verbose_name="简介")
    lifetime = RichTextField(blank=True, verbose_name="生平")
    achievement = RichTextField(blank=True, verbose_name="成就")
    result = models.SmallIntegerField(default=0,
                                      choices=(
                                          (0, "待处理"),
                                          (1, "已收录"),
                                          (2, "暂不收录")
                                      ), verbose_name="处理结果")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        verbose_name = "诗人推荐收录"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s.%s"%(self.name,self.dynasty)


class PerfectPoet(models.Model):
    user = models.ForeignKey('user.User', blank=True, null=True, on_delete=models.CASCADE, verbose_name="用户")
    poet = models.ForeignKey(Poet, on_delete=models.CASCADE, verbose_name="诗人")
    other_name = models.CharField(max_length=50, blank=True, verbose_name="别称")
    image = models.ImageField(upload_to="Poet/perfect/%Y/%m/%d/",blank=True, max_length=200, verbose_name="肖像")
    born = models.IntegerField(blank=True, null=True, verbose_name="生于")
    death = models.IntegerField(blank=True, null=True, verbose_name="卒于")
    introduce = RichTextField(blank=True, verbose_name="简介")
    lifetime = RichTextField(blank=True, verbose_name="生平")
    achievement = RichTextField(blank=True, verbose_name="成就")
    result = models.SmallIntegerField(default=0,
                                      choices=(
                                          (0, "待处理"),
                                          (1, "已完善"),
                                          (2, "暂不处理")
                                      ), verbose_name="处理结果")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        verbose_name = "完善诗人信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.poet.name


class PerfectPoem(models.Model):
    user = models.ForeignKey('user.User', blank=True, null=True, on_delete=models.CASCADE, verbose_name="用户")
    poem = models.ForeignKey(Poem, on_delete=models.CASCADE, verbose_name="诗歌")
    image = models.ImageField(upload_to="Poem/perfect/%Y/%m/%d/", blank=True, max_length=200, verbose_name="情景图片")
    tag = models.CharField(max_length=300, blank=True, verbose_name="标签")
    background = RichTextField(blank=True, verbose_name="背景")
    appreciation = RichTextField(blank=True, verbose_name="鉴赏")
    annotation = RichTextField(blank=True, verbose_name="注解")
    translation = RichTextField(blank=True, verbose_name="译文")
    result = models.SmallIntegerField(default=0,
                                      choices=(
                                          (0, "待处理"),
                                          (1, "已完善"),
                                          (2, "暂不处理")
                                      ), verbose_name="处理结果")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        verbose_name = "完善诗歌信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.poem.title