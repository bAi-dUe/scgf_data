from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model
from datetime import datetime

User = get_user_model()
# Create your models here.


class Notification(models.Model):
    title = models.CharField(max_length=30, blank=True, null=True, verbose_name="标题")
    content = models.CharField(max_length=300, verbose_name="通知内容")
    push = models.BooleanField(default=True, verbose_name="是否推送")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="时间")

    class Meta:
        verbose_name = "通知"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Banner(models.Model):
    title = models.CharField(max_length=50, verbose_name=u"标题")
    image = models.ImageField(upload_to="banner/%Y/%m", blank=True, verbose_name=u"轮播图", max_length=200)
    url = models.URLField(max_length=200, verbose_name=u"访问地址")
    index = models.IntegerField(default=100, verbose_name=u"顺序")
    show = models.BooleanField(default=True, verbose_name="是否展示")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Feedback(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, verbose_name="用户")
    subject = models.CharField(max_length=30, verbose_name="反馈主题")
    desc = RichTextUploadingField(verbose_name="问题描述")
    image = models.ImageField(upload_to="feedback/%Y/%m", max_length=200, blank=True, verbose_name="相关图片")
    contact = models.CharField(max_length=50, blank=True, verbose_name="联系方式")
    result = models.SmallIntegerField(default=0,
                                      choices=(
                                          (0, "待处理"),
                                          (1, "代办"),
                                          (2, "已处理"),
                                      ), verbose_name="处理结果")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name=u"添加时间")

    class Meta:
        verbose_name = "意见反馈"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.subject