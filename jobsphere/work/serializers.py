from rest_framework import serializers
from work.models import Work

class android_serializer(serializers.ModelSerializer):
    class Meta:
        model=Work
        fields='__all__'