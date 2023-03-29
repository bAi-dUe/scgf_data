from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import (
    CollectPoem,
    CollectPoet,
    CollectDynamic,
    CollectArticle,
    FabulousDynamic,
    FabulousArticle,
    FollowTopic,
    FollowUser,
    LikeComment,
    DislikeComment
)


@receiver(post_save, sender=CollectPoem)
def create_collect_poem(sender, instance=None, created=False, **kwargs):
    # instance 就是 Dynamic Model 实例
    if created:
        poem = instance.poem
        poem.fav_num += 1
        poem.save()


@receiver(post_delete, sender=CollectPoem)
def delete_collect_poem(sender, instance=None, created=False, **kwargs):
    poem = instance.poem
    poem.fav_num -= 1
    poem.save()


@receiver(post_save, sender=CollectPoet)
def create_collect_poet(sender, instance=None, created=False, **kwargs):
    if created:
        poet = instance.poet
        poet.fav_num += 1
        poet.save()


@receiver(post_delete, sender=CollectPoet)
def delete_collect_poet(sender, instance=None, created=False, **kwargs):
    poet = instance.poet
    poet.fav_num -= 1
    poet.save()


@receiver(post_save, sender=CollectDynamic)
def create_collect_dynamic(sender, instance=None, created=False, **kwargs):
    if created:
        dynamic = instance.dynamic
        dynamic.fav_num += 1
        dynamic.save()
        # 收藏动态会让发表该动态的用户增加5积分
        user = dynamic.user
        user.integral += 5
        user.save()


@receiver(post_delete, sender=CollectDynamic)
def delete_collect_dynamic(sender, instance=None, created=False, **kwargs):
    dynamic = instance.dynamic
    dynamic.fav_num -= 1
    dynamic.save()
    # 取消收藏动态会让发表该动态的用户减少5积分
    if dynamic.deleted is False:
        user = dynamic.user
        user.integral -= 5
        user.save()


@receiver(post_save, sender=CollectArticle)
def create_collect_article(sender, instance=None, created=False, **kwargs):
    if created:
        article = instance.article
        article.fav_num += 1
        article.save()
        # 收藏文章会让发表该文章的用户增加5积分
        user = article.user
        user.integral += 5
        user.save()


@receiver(post_delete, sender=CollectArticle)
def delete_collect_article(sender, instance=None, created=False, **kwargs):
    article = instance.article
    article.fav_num -= 1
    article.save()
    # 取消文章收藏会让发表该文章的用户减少5积分
    if article.deleted is False:
        user = article.user
        user.integral -= 5
        user.save()


@receiver(post_save, sender=FabulousDynamic)
def create_fabulous_dynamic(sender, instance=None, created=False, **kwargs):
    if created:
        # 动态增加点赞数
        dynamic = instance.dynamic
        dynamic.fabulous_num += 1
        dynamic.save()
        # 用户增加1获赞数和3积分
        user = dynamic.user
        user.fabulous_num += 1
        user.integral += 2
        user.save()


@receiver(post_delete, sender=FabulousDynamic)
def delete_fabulous_dynamic(sender, instance=None, created=False, **kwargs):
    # 动态减少 点赞数
    dynamic = instance.dynamic
    dynamic.fabulous_num -= 1
    dynamic.save()
    # 用户减少 1获赞数和3积分
    if dynamic.deleted is False:
        user = dynamic.user
        user.fabulous_num -= 1
        user.integral -= 2
        user.save()


@receiver(post_save, sender=FabulousArticle)
def create_fabulous_article(sender, instance=None, created=False, **kwargs):
    if created:
        # 文章增加点赞数
        article = instance.article
        article.fabulous_num += 1
        article.save()
        # 用户增加1获赞数和2积分
        user = article.user
        user.fabulous_num += 1
        user.integral += 2
        user.save()


@receiver(post_delete, sender=FabulousArticle)
def delete_fabulous_article(sender, instance=None, created=False, **kwargs):
    # 文章减少点赞数
    article = instance.article
    article.fabulous_num -= 1
    article.save()
    # 用户减少 1获赞数和2积分
    if article.deleted is False:
        user = article.user
        user.fabulous_num -= 1
        user.integral -= 2
        user.save()


@receiver(post_save, sender=FollowTopic)
def create_follow_topic(sender, instance=None, created=False, **kwargs):
    if created:
        topic = instance.topic
        topic.followed += 1
        topic.save()


@receiver(post_delete, sender=FollowTopic)
def delete_follow_topic(sender, instance=None, created=False, **kwargs):
    topic = instance.topic
    topic.followed -= 1
    topic.save()


@receiver(post_save, sender=FollowUser)
def create_follow_user(sender, instance=None, created=False, **kwargs):
    if created:
        # 用户增加关注人数
        user = instance.user
        user.follower += 1
        user.save()
        # 被关注用户增加 粉丝人数和10积分
        followed_user = instance.followed_user
        followed_user.fans += 1
        followed_user.integral += 10
        followed_user.save()


@receiver(post_delete, sender=FollowUser)
def delete_follow_user(sender, instance=None, created=False, **kwargs):
    # 用户减少 关注人数
    user = instance.user
    user.follower -= 1
    user.save()
    # 被关注用户减少 粉丝人数和10积分
    followed_user = instance.followed_user
    followed_user.fans -= 1
    followed_user.integral -= 10
    followed_user.save()


@receiver(post_save, sender=LikeComment)
def create_like_comment(sender, instance=None, created=False, **kwargs):
    if created:
        # 增加评论点赞
        comment = instance.comment
        comment.like += 1
        comment.save()

        user = comment.user
        user.fabulous_num += 1
        user.integral += 2
        user.save()


@receiver(post_delete, sender=LikeComment)
def delete_like_comment(sender, instance=None, created=False, **kwargs):
    comment = instance.comment
    comment.like -= 1
    comment.save()

    if comment.deleted is False:
        user = comment.user
        user.fabulous_num -= 1
        user.integral -= 2
        user.save()


@receiver(post_save, sender=DislikeComment)
def create_dislike_comment(sender, instance=None, created=False, **kwargs):
    if created:
        # 踩
        comment = instance.comment
        comment.dislike += 1
        comment.save()


@receiver(post_delete, sender=DislikeComment)
def delete_dislike_comment(sender, instance=None, created=False, **kwargs):
    comment = instance.comment
    comment.dislike -= 1
    comment.save()