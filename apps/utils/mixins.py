from rest_framework.response import Response
from rest_framework import status


class AddOneToClickNumRetrieveModelMixin(object):
    """
    Retrieve a model instance. and
        add 1 to click_num
    """
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.click_num += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class AddOneToClickNumAndIsOpRetrieveModelMixin(object):
    # self.foreign_model : string   用户收藏操作中的外键字段
    # OpModels : list   用户操作模型列表
    # op_fields : 需要修改的操作字段 如is_fabulous is_collect is_follow  (Bool)
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.click_num += 1
        instance.save()

        if request.user.is_authenticated:
            d = {
                "user": request.user,
                self.foreign_model: instance,
            }
            for index, OpModel in enumerate(self.OpModels):
                if OpModel.objects.filter(**d).exists():
                    setattr(instance, self.op_fields[index], True)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class IsOpRetrieveModelMixin(object):
    # self.foreign_model : string   用户收藏操作中的外键字段
    # OpModels : list   用户操作模型列表
    # op_fields : 需要修改的操作字段 如is_fabulous is_collect is_follow  (Bool)
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        if request.user.is_authenticated:
            d = {
                "user": request.user,
                self.foreign_model: instance,
            }
            for index, OpModel in enumerate(self.OpModels):
                if OpModel.objects.filter(**d).exists():
                    setattr(instance, self.op_fields[index], True)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class OpListModelMixin(object):
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            if request.user.is_authenticated:
                for instance in page:
                    d = {
                        "user": request.user,
                        self.foreign_model: instance,
                    }
                    for index, OpModel in enumerate(self.OpModels):
                        if OpModel.objects.filter(**d).exists():
                            setattr(instance, self.op_fields[index], True)
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        if request.user.is_authenticated:
            for instance in queryset:
                d = {
                    "user": request.user,
                    self.foreign_model: instance,
                }
                for index, OpModel in enumerate(self.OpModels):
                    if OpModel.objects.filter(**d).exists():
                        setattr(instance, self.op_fields[index], True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class LogicDestroyModelMixin(object):
    """
    Destroy a model instance.
    """
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.deleting = True
        instance.deleted = True
        instance.save()