import random

from django.core.mail import send_mail

from Shicigefu.settings import EMAIL_FROM


def random_code(length=6):
    code_set = "1234567890"
    code = []
    for i in range(length):
        code.append(random.choice(code_set))

    return "".join(code)


def send_verify_mail(to_email, code, code_type=0):
    if code_type==0:
        subject = "诗词歌赋-账号注册"
        message = "您正在注册诗词歌赋账号，验证码为 {code} ，5分钟内有效。".format(code=code)
        status = send_mail(subject, message, EMAIL_FROM, [to_email])
        return status
    elif code_type==1:
        subject = "诗词歌赋-找回密码"
        message = "您正在通过邮箱验证找回密码，验证码为 {code} ，5分钟内有效。".format(code=code)
        status = send_mail(subject, message, EMAIL_FROM, [to_email])
        return status