from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()


# 通过信号量机制，实现密码加密
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        # instance就是user
        password = instance.password
        instance.set_password(password)
        instance.save()
    else:
        # created为False，更新操作
        if instance.integral <= 500 and instance.designation != 1:
            instance.designation = 1
            instance.save()
        if 500 < instance.integral <= 2000 and instance.designation != 2:
            instance.designation = 2
            instance.save()
        if 2000 < instance.integral <= 8000 and instance.designation != 3:
            instance.designation = 3
            instance.save()
        if 8000 < instance.integral <= 20000 and instance.designation != 4:
            instance.designation = 4
            instance.save()
        if 20000 < instance.integral <= 50000 and instance.designation != 5:
            instance.designation = 5
            instance.save()
        if instance.integral > 50000 and instance.designation!=6:
            instance.designation = 6
            instance.save()