from rest_framework.response import Response


class RetrieveAndAddClickNumModelMixin(object):
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