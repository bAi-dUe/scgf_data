from datetime import datetime, timedelta

from django.contrib.auth import get_user_model

from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status as http_status

from .models import MailVerifyCode
from .serializers import MailVerifyCodeSerializer
from .utils import random_code, send_verify_mail

User = get_user_model()
# Create your views here.


class MailVerifyCodeViewSet(mixins.CreateModelMixin,
                            viewsets.GenericViewSet):
    serializer_class = MailVerifyCodeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data["email"]
        code_type = serializer.validated_data["code_type"]
        code = random_code()
        status = send_verify_mail(email, code, code_type)

        if status:
            MailVerifyCode(email=email, code=code, code_type=code_type).save()
            return Response({
                "type": code_type,
                "status_code": 0,
                "msg": "发送成功"
            }, status=http_status.HTTP_201_CREATED)
        else:
            return Response({
                "type": code_type,
                "status_code": 1,
                "msg": "发送失败"
            }, status=http_status.HTTP_400_BAD_REQUEST)