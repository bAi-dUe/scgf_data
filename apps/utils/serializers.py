from rest_framework import serializers

class OnlyIdSerializer(serializers.Serializer):
    id = serializers.IntegerField()