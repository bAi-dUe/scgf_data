from django.db import models
from django.contrib.auth import get_user_model

from poetry.models import (
    Poem,
    Poet
)
from community.models import (
    Topic,
    Dynamic,
    Article,
    Comment
)

User = get_user_model()

# Create your models here.


class Base:
    def get_username(self):
        return self.user.email


class CollectPoem(models.Model, Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    poem = models.ForeignKey(Poem, on_delete=models.CASCADE, verbose_name="诗歌", help_text="诗歌id")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    def get_poem_title(self):
        return self.poem.title

    class Meta:
        verbose_name = "收藏诗歌"
        verbose_name_plural = verbose_name
        unique_together = ("user", "poem")


class CollectPoet(models.Model, Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    poet = models.ForeignKey(Poet, on_delete=models.CASCADE, verbose_name="诗人", help_text="诗人id")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    def get_poet_name(self):
        return self.poet.name

    class Meta:
        verbose_name = "收藏诗人"
        verbose_name_plural = verbose_name
        unique_together = ("user", "poet")


class CollectDynamic(models.Model, Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    dynamic = models.ForeignKey(Dynamic, on_delete=models.CASCADE, verbose_name="动态")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    def get_dynamic_subject(self):
        return self.dynamic.subject

    class Meta:
        verbose_name = "收藏动态"
        verbose_name_plural = verbose_name
        unique_together = ("user", "dynamic")


class FabulousDynamic(models.Model, Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    dynamic = models.ForeignKey(Dynamic, on_delete=models.CASCADE, verbose_name="动态")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    def get_dynamic_subject(self):
        return self.dynamic.subject

    class Meta:
        verbose_name = "点赞-动态"
        verbose_name_plural = verbose_name
        unique_together = ("user", "dynamic")


class CollectArticle(models.Model, Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="动态")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    def get_article_title(self):
        return self.article.title

    class Meta:
        verbose_name = "收藏文章"
        verbose_name_plural = verbose_name
        unique_together = ("user", "article")


class FabulousArticle(models.Model, Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="动态")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    def get_article_title(self):
        return self.article.title

    class Meta:
        verbose_name = "收藏文章"
        verbose_name_plural = verbose_name
        unique_together = ("user", "article")


class FollowTopic(models.Model, Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name="话题")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    def get_topic_name(self):
        return self.topic.topic

    class Meta:
        verbose_name = "关注话题"
        verbose_name_plural = verbose_name
        unique_together = ("user", "topic")


class FollowUser(models.Model, Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户", related_name="user_fans")
    followed_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="被关注者", related_name="user_follow", help_text="用户id")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    def get_followed_user_name(self):
        return self.followed_user.email

    class Meta:
        verbose_name = "关注用户"
        verbose_name_plural = verbose_name
        unique_together = ("user", "followed_user")


class LikeComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, verbose_name="评论")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        verbose_name = "赞-评论"
        verbose_name_plural = verbose_name
        unique_together = ("user", "comment")


class DislikeComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, verbose_name="评论")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        verbose_name = "踩-评论"
        verbose_name_plural = verbose_name
        unique_together = ("user", "comment")