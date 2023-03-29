from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.


class MailVerifyCode(models.Model):
    email = models.EmailField(verbose_name="接收邮箱")
    code = models.CharField(max_length=6,verbose_name="验证码")
    code_type = models.IntegerField(choices=((0,"注册"),(1,"找回密码")), default=0, verbose_name="验证码类型")
    send_time = models.DateTimeField(auto_now_add=True, verbose_name="发送时间")

    def __str__(self):
        return "Code<{}>".format(self.code)

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name


class SMSVerifyCode(models.Model):
    phone = models.CharField(max_length=11, validators=[MinLengthValidator(11)], verbose_name="手机")
    code = models.CharField(max_length=6,verbose_name="验证码")
    code_type = models.IntegerField(choices=((0,"注册"),(1,"找回密码")), default=0, verbose_name="验证码类型")
    send_time = models.DateTimeField(auto_now_add=True, verbose_name="发送时间")

    class Meta:
        verbose_name = "短信验证码"
        verbose_name_plural = verbose_name