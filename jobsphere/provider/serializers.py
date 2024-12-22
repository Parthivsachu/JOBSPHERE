from rest_framework import serializers
from provider.models import Provider

class android_serializer(serializers.ModelSerializer):
    class Meta:
        model=Provider
        fields='__all__'