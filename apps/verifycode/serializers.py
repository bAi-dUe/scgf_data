from datetime import datetime, timedelta

from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import MailVerifyCode

User = get_user_model()


class MailVerifyCodeSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, label="邮箱")
    code_type = serializers.ChoiceField(choices=((0, "注册账号"), (1, "忘记密码")),
                                        default=0,
                                        label="验证码类型",
                                        help_text="验证码类型(数字)：1为注册账号，2为忘记密码")

    def validate(self, attrs):
        email = attrs["email"]
        code_type = attrs["code_type"]
        if code_type == 0:
            if User.objects.filter(email=email).exists():
                raise serializers.ValidationError({
                    "type": code_type,
                    "status_code": 2,
                    "msg": "该邮箱已注册"
                })

            codes = MailVerifyCode.objects.filter(email=email, code_type=code_type).order_by('-send_time')
            if codes.exists():
                #取最新的一条验证码
                code = codes[0]
                delta = timedelta(minutes=1)
                if code.send_time + delta > datetime.now():
                    #1分钟内无须重复发送邮箱验证码
                    raise serializers.ValidationError({
                        "type": code_type,
                        "status_code": 3,
                        "msg": "已发送邮箱验证码，请不要重复发送"
                    }, )
        elif code_type == 1:
            if not User.objects.filter(email=email).exists():
                raise serializers.ValidationError({
                    "type": code_type,
                    "status_code": 4,
                    "msg": "此邮箱未注册"
                })

            codes = MailVerifyCode.objects.filter(email=email, code_type=code_type).order_by('-send_time')
            if codes.exists():
                code = codes[0]
                delta = timedelta(minutes=1)
                if code.send_time + delta > datetime.now():
                    raise serializers.ValidationError({
                        "type": code_type,
                        "status_code": 3,
                        "msg": "已发送邮箱验证码，请不要重复发送"
                    }, )

        return attrs