from rest_framework import serializers
from labour.models import Labour

class android_serializer(serializers.ModelSerializer):
    class Meta:
        model=Labour
        fields='__all__'