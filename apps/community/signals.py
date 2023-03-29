from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import (
    Dynamic,
    Article,
    Sign,
    Comment
)


@receiver(post_save, sender=Dynamic)
def dynamic(sender, instance=None, created=False, **kwargs):
    # instance 就是 Dynamic Model 实例
    if created:
        if instance.topic is not None:
            topic = instance.topic
            topic.nums += 1
            topic.save()
        # 发表动态增加20积分
        user = instance.user
        user.integral += 20
        user.save()
    # 更新操作
    else:
        # 如果为删除动作
        if instance.deleting is True:
            if instance.topic is not None:
                topic = instance.topic
                topic.nums -= 1
                topic.save()
            # 删除动态会扣除已获得积分及获赞数
            user = instance.user
            # 动态 20 点赞数*2 （评论数+收藏数）*5
            integral = 20 + instance.fabulous_num*2 + (instance.fav_num+instance.comment_num)*5
            user.integral -= integral
            # 减少获赞数
            user.fabulous_num -= instance.fabulous_num
            user.save()
            # 逻辑删除成功
            instance.deleting = False
            instance.save()


@receiver(post_save, sender=Article)
def article(sender, instance=None, created=False, **kwargs):
    if created:
        # 发表文章增加20积分
        user = instance.user
        user.integral += 20
        user.save()
    # 更新操作
    else:
        # 删除动作
        if instance.deleting is True:
            user = instance.user
            integral = 20 + instance.fabulous_num * 2 + (instance.fav_num + instance.comment_num) * 5
            user.integral -= integral
            user.fabulous_num -= instance.fabulous_num
            user.save()
            # 删除成功
            instance.deleting = False
            instance.save()


@receiver(post_save, sender=Sign)
def sign_in_per_day(sender, instance=None, created=False, **kwargs):
    if created:
        # 发表文章增加20积分
        user = instance.user
        user.integral += 10
        user.save()


@receiver(post_save, sender=Comment)
def comment(sender, instance=None, created=False, **kwargs):
    # 评论增加5点积分
    if created:
        f_instance = instance.content_object
        f_instance.comment_num += 1
        f_instance.save()

        user = f_instance.user
        user.integral += 5
        user.save()
    # 更新
    else:
        # 删除操作
        if instance.deleting is True:
            user = instance.user
            integral = instance.like*2 + instance.comment_num*5
            user.integral -= integral
            user.fabulous_num -= instance.like
            user.save()

            father_instance = instance.content_object
            father_instance.comment_num -= 1
            father_instance.save()
            if father_instance.deleted is False:
                f_user = father_instance.user
                f_user.integral -= 5
                f_user.save()

            instance.deleting = False
            instance.save()


# @receiver(post_delete, sender=Comment)
# def delete_comment(sender, instance=None, created=False, **kwargs):
#     # 评论减少5点积分
#     user = instance.user
#     user.fabulous_num -= instance.like
#     user.integral -= instance.like
#     user.integral -= instance.comment_num*5
#     f_instance = instance.content_object
#     if f_instance is None:
#         return
#     f_instance.comment_num -= 1
#     f_instance.save()
#
#     user = f_instance.user
#     user.integral -= 5
#     user.save()

