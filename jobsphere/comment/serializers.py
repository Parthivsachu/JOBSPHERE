from rest_framework import serializers
from comment.models import Comment

class android_serializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields='__all__'