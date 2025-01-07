from rest_framework import serializers

class FormSerializer(serializers.Serializer):
    fields=serializers.DictField(child=serializers.CharField())