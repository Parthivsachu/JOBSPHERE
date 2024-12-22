from rest_framework import serializers
from consumer.models import Consumer

class android_serializer(serializers.ModelSerializer):
    class Meta:
        model=Consumer
        fields='__all__'